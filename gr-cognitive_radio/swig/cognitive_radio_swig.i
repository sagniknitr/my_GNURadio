/* -*- c++ -*- */

#define COGNITIVE_RADIO_API

%include "gnuradio.i"			// the common stuff

//load generated python docstrings
%include "cognitive_radio_swig_doc.i"

%{
#include "cognitive_radio/ED.h"
#include "cognitive_radio/noise_average_sink.h"
%}


%include "cognitive_radio/ED.h"
GR_SWIG_BLOCK_MAGIC2(cognitive_radio, ED);
%include "cognitive_radio/noise_average_sink.h"
GR_SWIG_BLOCK_MAGIC2(cognitive_radio, noise_average_sink);
