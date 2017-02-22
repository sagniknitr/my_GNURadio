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

#ifdef HAVE_CONFIG_H
#include "config.h"
#endif

#include <gnuradio/io_signature.h>
#include "ED_impl.h"
#include <iostream>

using namespace std;

#define SAMPLES 4096
#define PFA 13
#define STEP 1


namespace gr {
  namespace cognitive_radio {

    ED::sptr
    ED::make(int samplesperstream, std::vector<float> noisevar, int
prob_false_alarm, int fftsize, int streams)


    {
      return gnuradio::get_initial_sptr
        (new ED_impl(samplesperstream, noisevar, prob_false_alarm,
fftsize, streams));
    }

    /*
     * The private constructor
     */
    ED_impl::ED_impl(int samplesperstream, std::
vector<float> noisevar, int prob_false_alarm, int fftsize, int streams)

      : gr::block("ED",
              gr::io_signature::make(1, 1, fftsize * sizeof (gr_complex)),
              gr::io_signature::make3(3, 3, streams * sizeof (float), streams * sizeof (float),
streams * sizeof (short))),sps(samplesperstream), d_noisevar(noisevar), d_prob_false_alarm(
prob_false_alarm), d_fftsize(fftsize), d_streams(streams)                                      //some changes may be required here

    {
		    	set_relative_rate(1.0);
		threshold = new float*[PFA];
		for(int k=0;k<PFA;k++)
		threshold[k] = new float [SAMPLES];

		if ((fp = fopen ("threshold.dat","rb")) == NULL)
		{
		cout << "File vuoto\n" << endl;
		}
		for (int i=0;i<PFA;i++)
		fread(threshold[i],sizeof(float),SAMPLES,fp);
		fclose(fp);
}

    /*
     * Our virtual destructor.
     */
    ED_impl::~ED_impl()
    {
		    	for(int k=0;k<PFA;k++)
		delete [] threshold;
		delete [] threshold;



    }

    	void ED_impl::set_noisevar(std::vector<float> noisevar)
{
d_noisevar = noisevar;
}




    void
    ED_impl::forecast (int noutput_items, gr_vector_int &ninput_items_required)
    {
      /* <+forecast+> e.g. ninput_items_required[0] = noutput_items */
    	ninput_items_required[0] = noutput_items;
    }

    int
    ED_impl::general_work (int noutput_items,
                       gr_vector_int &ninput_items,
                       gr_vector_const_void_star &input_items,
                       gr_vector_void_star &output_items)
    {


if((sps % STEP!=0) || (sps>SAMPLES)) {
printf("Samples must be multiple of 10 and less than %d.\n", SAMPLES);
return -1;
}
if(d_streams != d_noisevar.size()) {
cout << "Number of streams and noise vector size DON’T match." << endl;
return -1;
}
if(sps*d_streams > d_fftsize) {
cout << "Too many samples per stream." << endl;
return -1;
}
gr_complex *in = (gr_complex *) input_items[0];
float *out0= (float *) output_items[0];
float *out1= (float *) output_items[1];
short *out2= (short *) output_items[2];
float T_ED[d_streams];
int z = 0;
int col = sps/STEP-1;
//int start_index = (d_fftsize - sps∗d_streams) / 2 - 1;
int start_index=(d_fftsize-sps*d_streams)/2-1;
if (start_index < 0)
start_index = 0;
while(z < noutput_items) {
in += start_index;
memset(T_ED, 0, d_streams *sizeof(float));
for(int i=0; i<d_streams; i++){
for(int j=i*sps; j<(i+1)*sps; j++) {
T_ED[i] += abs(in[j]*conj(in[j]));
}
float temp = T_ED[i]/(d_fftsize*sps);
out1[i] = temp;
out0[i] = temp/d_noisevar[i];
if(out0[i]>threshold[d_prob_false_alarm][col])
out2[i] = 1;
else
out2[i] = 0;
}
in += d_fftsize;
out0 += d_streams;
out1 += d_streams;
out2 += d_streams;
z++;
    }

    consume_each (noutput_items);
return noutput_items;

  } /* namespace cognitive_radio */
} /* namespace gr */
}
