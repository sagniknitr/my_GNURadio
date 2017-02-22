/* -*- c++ -*- */
/* 
 * Copyright 2016 <+YOU OR YOUR COMPANY+>.
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

#ifndef INCLUDED_COGNITIVE_RADIO_NOISE_AVERAGE_SINK_IMPL_H
#define INCLUDED_COGNITIVE_RADIO_NOISE_AVERAGE_SINK_IMPL_H

#include <cognitive_radio/noise_average_sink.h>

namespace gr {
  namespace cognitive_radio {

    class noise_average_sink_impl : public noise_average_sink
    {
     private:

      int *current_slots;
      int d_slots;
      int d_consecutive;
      float *average;
      int d_veclen;
      std::vector<float> noise;



      // Nothing to declare in this block.

     public:
      noise_average_sink_impl(int slots,int consecutive,int veclen);
      ~noise_average_sink_impl();
      std::vector<float> get_noise();
      float get_noise_subband();

      // Where all the action really happens
      void forecast (int noutput_items, gr_vector_int &ninput_items_required);

      int general_work(int noutput_items,
           gr_vector_int &ninput_items,
           gr_vector_const_void_star &input_items,
           gr_vector_void_star &output_items);
    };

  } // namespace cognitive_radio
} // namespace gr

#endif /* INCLUDED_COGNITIVE_RADIO_NOISE_AVERAGE_SINK_IMPL_H */

