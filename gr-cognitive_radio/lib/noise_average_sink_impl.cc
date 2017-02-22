
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

#ifdef HAVE_CONFIG_H
#include "config.h"
#endif

#include <gnuradio/io_signature.h>
#include "noise_average_sink_impl.h"

using namespace std;

namespace gr {
  namespace cognitive_radio {

    noise_average_sink::sptr
    noise_average_sink::make(int slots, int consecutive, int veclen)
    {
      return gnuradio::get_initial_sptr
        (new noise_average_sink_impl(slots,consecutive,veclen));
    }

    /*
     * The private constructor
     */
    noise_average_sink_impl::noise_average_sink_impl(int slots,int consecutive,int veclen)
      : gr::block("noise_average_sink",
              gr::io_signature::make(2, 2, veclen*sizeof(float)),//veclen*sizeof(short)),
              gr::io_signature::make(0, 0, 0))
              //d_slots(slots), d_consecutive(consecutive), d_veclen(veclen)
    {
      noise.resize(d_veclen);
      average = new float [d_veclen];
      current_slots = new int [d_veclen];
      memset(average, 0, d_veclen*sizeof(float));
      memset(current_slots, 0, d_veclen*sizeof(int));
      for(int i=0;i<d_veclen; i++)
      noise[i] = 25e-9;
    }

    /*
     * Our virtual destructor.
     */
    noise_average_sink_impl::~noise_average_sink_impl()
    {
      delete [] average;
      delete [] current_slots;
    }

      std::vector<float> noise_average_sink_impl::get_noise() {
          return noise;
}

      float noise_average_sink_impl::get_noise_subband() {
return noise[0];
}




   void noise_average_sink_impl::forecast (int noutput_items, gr_vector_int &ninput_items_required)
    {
      /* <+forecast+> e.g. ninput_items_required[0] = noutput_items */
    }

    int noise_average_sink_impl::general_work (int noutput_items,
                       gr_vector_int &ninput_items,
                       gr_vector_const_void_star &input_items,
                       gr_vector_void_star &output_items)
    {
      const float *in0 = (const float *) input_items[0];
      const short *in1 = (const short *) input_items[1];
      int z=0;
      while (z< noutput_items)
      {
        for(int i=0;i<d_veclen;i++)
        {
          if(in1[i]==0)
          {
            average[i]+=in0[i];
            current_slots[i]++;
            if(current_slots[i]==d_slots)
            {
              noise[i]=average[i]/d_slots;
              current_slots[i]=0;
              average[i]=0.0;
            }
          }
          else
          {
            if(d_consecutive==1)
            {
              average[i]=0.0;
              current_slots[i]=0;

            }
          }
        }
        in0+=d_veclen;
        in1 +=d_veclen;
        z++;
      }

      //<+OTYPE+> *out = (<+OTYPE+> *) output_items[0];

      // Do <+signal processing+>
      // Tell runtime system how many input items we consumed on
      // each input stream.
      //consume_each (noutput_items);

      // Tell runtime system how many output items we produced.
      return noutput_items;
    }

  } /* namespace cognitive_radio */
} /* namespace gr */

