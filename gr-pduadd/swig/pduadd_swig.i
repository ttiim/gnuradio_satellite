/* -*- c++ -*- */

#define PDUADD_API

%include "gnuradio.i"           // the common stuff

//load generated python docstrings
%include "pduadd_swig_doc.i"

%{
#include "pduadd/pdu_head_tail.h"
%}

%include "pduadd/pdu_head_tail.h"
GR_SWIG_BLOCK_MAGIC2(pduadd, pdu_head_tail);
