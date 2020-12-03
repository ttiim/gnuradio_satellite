/* -*- c++ -*- */
/*
 * Copyright 2020 gr-pduadd author.
 *
 * This is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3, or (at your option)
 * any later version.
 *
 * This software is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this software; see the file COPYING.  If not, write to
 * the Free Software Foundation, Inc., 51 Franklin Street,
 * Boston, MA 02110-1301, USA.
 */

#ifdef HAVE_CONFIG_H
#include "config.h"
#endif

#include <gnuradio/io_signature.h>
#include "crc16_impl.h"

#include <algorithm>
#include <vector>
#include <string>

namespace gr {
  namespace pduadd {

    crc16::sptr crc16::make()
    {
      return gnuradio::get_initial_sptr(new crc16_impl());
    }


    /*
     * The private constructor
     */
    crc16_impl::crc16_impl()
      : gr::block("crc16",
              gr::io_signature::make(0, 0, 0),
              gr::io_signature::make(0, 0, 0))
    {
    message_port_register_out(pmt::mp("out"));
    message_port_register_in(pmt::mp("in"));
    set_msg_handler(pmt::mp("in"), [this](pmt::pmt_t msg) { this->msg_handler(msg); });
    }

    /*
     * Our virtual destructor.
     */
    crc16_impl::~crc16_impl() {}

    void
    crc16_impl::forecast (int noutput_items, gr_vector_int &ninput_items_required) {}

    int
    crc16_impl::general_work (int noutput_items,
                       gr_vector_int &ninput_items,
                       gr_vector_const_void_star &input_items,
                       gr_vector_void_star &output_items)
    {
      return 0;
    }
    
    uint16_t culCalcCRC(unsigned char crcData, uint16_t crcReg) {
        uint8_t i;
        for (i = 0; i < 8; i++) {
            if (((crcReg & 0x8000) >> 8) ^ (crcData & 0x80))
                crcReg = (crcReg << 1) ^ 0x8005;
            else
                crcReg = (crcReg << 1);
            crcData <<= 1;
        }
        return crcReg;
    }
    
    void crc16_impl::msg_handler(pmt::pmt_t pmt_msg)
    {
    std::vector<uint8_t> msg = pmt::u8vector_elements(pmt::cdr(pmt_msg));
    std::vector<uint8_t> cut_msg = std::vector<uint8_t>(msg.begin(), msg.end());
    uint16_t checksum;
    uint8_t i;
    checksum = 0xFFFF; // Init value for CRC calculation
    for (i = 0; i < cut_msg.size(); i++)
        checksum = culCalcCRC(cut_msg[i], checksum);
    cut_msg.push_back(checksum);
    
    message_port_pub(
        pmt::mp("out"),
        pmt::cons(pmt::car(pmt_msg), pmt::init_u8vector(cut_msg.size(), cut_msg)));
    }

  } /* namespace pduadd */
} /* namespace gr */

