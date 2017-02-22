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


#ifndef INCLUDED_COGNITIVE_RADIO_ED_H
#define INCLUDED_COGNITIVE_RADIO_ED_H

#include <cognitive_radio/api.h>
#include <gnuradio/block.h>
#include <iostream>
#include <stdio.h>

namespace gr {
  namespace cognitive_radio {

    /*!
     * \brief <+description of block+>
     * \ingroup cognitive_radio
     *
     */
    class COGNITIVE_RADIO_API ED : virtual public gr::block
    {
     public:
      typedef boost::shared_ptr<ED> sptr;

      /*!
       * \brief Return a shared_ptr to a new instance of cognitive_radio::ED.
       *
       * To avoid accidental use of raw pointers, cognitive_radio::ED's
       * constructor is in a private implementation
       * class. cognitive_radio::ED::make is the public interface for
       * creating new instances.
       */
      static sptr make(int samplesperstream, std::vector<float> noisevar, int prob_false_alarm
      , int fftsize, int streams);
      virtual void set_noisevar(std::vector<float> noisevar) = 0;


      static sptr make();
    };

  } // namespace cognitive_radio
} // namespace gr

#endif /* INCLUDED_COGNITIVE_RADIO_ED_H */

