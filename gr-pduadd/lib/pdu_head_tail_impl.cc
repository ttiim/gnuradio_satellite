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
#include "pdu_head_tail_impl.h"

#include <algorithm>
#include <vector>
#include <string>

namespace gr {
  namespace pduadd {

    pdu_head_tail::sptr pdu_head_tail::make(std::string add)
    {
      return gnuradio::get_initial_sptr(new pdu_head_tail_impl(add));
    }


    /*
     * The private constructor
     */
    pdu_head_tail_impl::pdu_head_tail_impl(std::string add)
      : gr::block("pdu_head_tail",
              gr::io_signature::make(0, 0, 0),
              gr::io_signature::make(0, 0, 0)),
        d_add(add)
    {
    message_port_register_out(pmt::mp("out"));
    message_port_register_in(pmt::mp("in"));
    set_msg_handler(pmt::mp("in"), [this](pmt::pmt_t msg) { this->msg_handler(msg); });
    }

    /*
     * Our virtual destructor.
     */
    pdu_head_tail_impl::~pdu_head_tail_impl() {}

    void
    pdu_head_tail_impl::forecast (int noutput_items, gr_vector_int &ninput_items_required) {}

    int
    pdu_head_tail_impl::general_work (int noutput_items,
                       		gr_vector_int &ninput_items,
                       		gr_vector_const_void_star &input_items,
                       		gr_vector_void_star &output_items)
    {
      return 0;
    }
    
    void pdu_head_tail_impl::msg_handler(pmt::pmt_t pmt_msg)
    {
    std::vector<uint8_t> msg = pmt::u8vector_elements(pmt::cdr(pmt_msg));
    std::vector<uint8_t> cut_msg = std::vector<uint8_t>(msg.begin(), msg.end());
    auto add = d_add;
    
    while(add.length()){
    	std::string temp_add = add.substr(add.length()-8, 8);
    	add.erase(add.length()-8, add.length());
    	int int_add = std::stoi(temp_add);
    	int dec_value = 0;
    	int base = 1;
    	while (int_add) {
   		int last_digit = int_add % 10;
        	int_add = int_add / 10;
        	dec_value += last_digit * base;
        	base = base * 2;
    	}
    	cut_msg.insert(cut_msg.begin(), dec_value);
    	
    }
    message_port_pub(
        pmt::mp("out"),
        pmt::cons(pmt::car(pmt_msg), pmt::init_u8vector(cut_msg.size(), cut_msg)));
    }

} /* namespace pduadd */
} /* namespace gr */

