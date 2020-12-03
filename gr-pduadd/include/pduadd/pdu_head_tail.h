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

#ifndef INCLUDED_PDUADD_PDU_HEAD_TAIL_H
#define INCLUDED_PDUADD_PDU_HEAD_TAIL_H

#include <pduadd/api.h>
#include <gnuradio/block.h>

namespace gr {
  namespace pduadd {

    /*!
     * \brief <+description of block+>
     * \ingroup pduadd
     *
     */
    class PDUADD_API pdu_head_tail : virtual public gr::block
    {
     public:
      typedef boost::shared_ptr<pdu_head_tail> sptr;

      /*!
       * \brief Return a shared_ptr to a new instance of pduadd::pdu_head_tail.
       *
       * To avoid accidental use of raw pointers, pduadd::pdu_head_tail's
       * constructor is in a private implementation
       * class. pduadd::pdu_head_tail::make is the public interface for
       * creating new instances.
       */
      static sptr make(std::string add);
    };

  } // namespace pduadd
} // namespace gr

#endif /* INCLUDED_PDUADD_PDU_HEAD_TAIL_H */

