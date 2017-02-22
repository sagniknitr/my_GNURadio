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

#ifndef INCLUDED_COGNITIVE_RADIO_ED_IMPL_H
#define INCLUDED_COGNITIVE_RADIO_ED_IMPL_H

#include <cognitive_radio/ED.h>
#include <vector>

namespace gr {
  namespace cognitive_radio {

    class ED_impl : public ED
    {
     private:
      // Nothing to declare in this block.
      int sps;

      std::vector<float> d_noisevar;

        int d_prob_false_alarm;

        float **threshold;

        FILE *fp;

        int d_fftsize;

        int d_streams;  
     public:
      ED_impl(int samplesperstream, std::vector<float> noisevar, int
          prob_false_alarm, int fftsize, int streams);


      ~ED_impl();

      // Where all the action really happens
      void forecast (int noutput_items, gr_vector_int &ninput_items_required);
      void set_noisevar(std::vector<float> noisevar);
      int general_work(int noutput_items,
           gr_vector_int &ninput_items,
           gr_vector_const_void_star &input_items,
           gr_vector_void_star &output_items);
    };

  } // namespace cognitive_radio
} // namespace gr

#endif /* INCLUDED_COGNITIVE_RADIO_ED_IMPL_H */

