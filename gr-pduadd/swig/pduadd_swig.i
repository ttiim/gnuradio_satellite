/* -*- c++ -*- */

#define PDUADD_API

%include "gnuradio.i"           // the common stuff

//load generated python docstrings
%include "pduadd_swig_doc.i"

%{
#include "pduadd/pdu_head_tail.h"
#include "pduadd/crc16.h"
#include "pduadd/add_length.h"
#include "pduadd/usrp_pad.h"
%}

%include "pduadd/pdu_head_tail.h"
GR_SWIG_BLOCK_MAGIC2(pduadd, pdu_head_tail);
%include "pduadd/crc16.h"
GR_SWIG_BLOCK_MAGIC2(pduadd, crc16);
%include "pduadd/add_length.h"
GR_SWIG_BLOCK_MAGIC2(pduadd, add_length);

%include "pduadd/usrp_pad.h"
GR_SWIG_BLOCK_MAGIC2(pduadd, usrp_pad);
