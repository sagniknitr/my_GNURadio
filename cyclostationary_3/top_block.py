#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Fri Dec  2 10:51:44 2016
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from baz import facsink
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import fft
from gnuradio import filter
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.wxgui import forms
from gnuradio.wxgui import numbersink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import baz
import osmosdr
import time
import wx


class top_block(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Top Block")

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 1e5
        self.freq = freq = 500e06

        ##################################################
        # Blocks
        ##################################################
        _freq_sizer = wx.BoxSizer(wx.VERTICAL)
        self._freq_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_freq_sizer,
        	value=self.freq,
        	callback=self.set_freq,
        	label='freq',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._freq_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_freq_sizer,
        	value=self.freq,
        	callback=self.set_freq,
        	minimum=400e06,
        	maximum=600e06,
        	num_steps=1000,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_freq_sizer)
        self.wxgui_numbersink2_0 = numbersink2.number_sink_f(
        	self.GetWin(),
        	unit="Units",
        	minval=-100,
        	maxval=100,
        	factor=1.0,
        	decimal_places=10,
        	ref_level=0,
        	sample_rate=samp_rate,
        	number_rate=15,
        	average=False,
        	avg_alpha=None,
        	label="Number Plot",
        	peak_hold=False,
        	show_gauge=True,
        )
        self.Add(self.wxgui_numbersink2_0.win)
        self.osmosdr_source_0 = osmosdr.source( args="numchan=" + str(1) + " " + "" )
        self.osmosdr_source_0.set_sample_rate(samp_rate)
        self.osmosdr_source_0.set_center_freq(freq, 0)
        self.osmosdr_source_0.set_freq_corr(0, 0)
        self.osmosdr_source_0.set_dc_offset_mode(0, 0)
        self.osmosdr_source_0.set_iq_balance_mode(0, 0)
        self.osmosdr_source_0.set_gain_mode(False, 0)
        self.osmosdr_source_0.set_gain(10, 0)
        self.osmosdr_source_0.set_if_gain(20, 0)
        self.osmosdr_source_0.set_bb_gain(20, 0)
        self.osmosdr_source_0.set_antenna("", 0)
        self.osmosdr_source_0.set_bandwidth(0, 0)
          
        self.fft_vxx_0_0 = fft.fft_vcc(1024, True, (window.blackmanharris(1024)), True, 1)
        self.fft_vxx_0 = fft.fft_vcc(1024, True, (window.blackmanharris(1024)), True, 1)
        self.facsink_0 = facsink.fac_sink_c(
        	self.GetWin(),
        	title="Fast AutoCorrelation",
        	sample_rate=samp_rate,
        	baseband_freq=freq,
                y_per_div=10,
        	ref_level=50,
        	fac_size=512,
                fac_rate=facsink.default_fac_rate,
                average=False,
        	avg_alpha=0,
        	peak_hold=False,
        )
        self.Add(self.facsink_0.win)
        self.dc_blocker_xx_0 = filter.dc_blocker_cc(32, True)
        self.blocks_vector_to_stream_0_0 = blocks.vector_to_stream(gr.sizeof_gr_complex*1, 1024)
        self.blocks_vector_to_stream_0 = blocks.vector_to_stream(gr.sizeof_gr_complex*1, 1024)
        self.blocks_stream_to_vector_0_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, 1024)
        self.blocks_stream_to_vector_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, 1024)
        self.blocks_multiply_xx_0 = blocks.multiply_vff(1)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_float*1, "/home/nitr/Sagnik/gnuradio_data/cyclo_2.dat", False)
        self.blocks_file_sink_0.set_unbuffered(False)
        self.blocks_conjugate_cc_0 = blocks.conjugate_cc()
        self.blocks_complex_to_real_1_0 = blocks.complex_to_real(1)
        self.blocks_complex_to_real_1 = blocks.complex_to_real(1)
        self.baz_delay_0_0 = baz.delay(gr.sizeof_gr_complex*1, 1)
        self.baz_delay_0 = baz.delay(gr.sizeof_gr_complex*1, -1)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.baz_delay_0, 0), (self.blocks_stream_to_vector_0, 0))    
        self.connect((self.baz_delay_0_0, 0), (self.blocks_stream_to_vector_0_0, 0))    
        self.connect((self.blocks_complex_to_real_1, 0), (self.blocks_multiply_xx_0, 0))    
        self.connect((self.blocks_complex_to_real_1_0, 0), (self.blocks_multiply_xx_0, 1))    
        self.connect((self.blocks_conjugate_cc_0, 0), (self.baz_delay_0_0, 0))    
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_file_sink_0, 0))    
        self.connect((self.blocks_multiply_xx_0, 0), (self.wxgui_numbersink2_0, 0))    
        self.connect((self.blocks_stream_to_vector_0, 0), (self.fft_vxx_0, 0))    
        self.connect((self.blocks_stream_to_vector_0_0, 0), (self.fft_vxx_0_0, 0))    
        self.connect((self.blocks_vector_to_stream_0, 0), (self.blocks_complex_to_real_1, 0))    
        self.connect((self.blocks_vector_to_stream_0_0, 0), (self.blocks_complex_to_real_1_0, 0))    
        self.connect((self.dc_blocker_xx_0, 0), (self.baz_delay_0, 0))    
        self.connect((self.dc_blocker_xx_0, 0), (self.blocks_conjugate_cc_0, 0))    
        self.connect((self.dc_blocker_xx_0, 0), (self.facsink_0, 0))    
        self.connect((self.fft_vxx_0, 0), (self.blocks_vector_to_stream_0, 0))    
        self.connect((self.fft_vxx_0_0, 0), (self.blocks_vector_to_stream_0_0, 0))    
        self.connect((self.osmosdr_source_0, 0), (self.dc_blocker_xx_0, 0))    

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.osmosdr_source_0.set_sample_rate(self.samp_rate)
        self.facsink_0.set_sample_rate(self.samp_rate)

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self._freq_slider.set_value(self.freq)
        self._freq_text_box.set_value(self.freq)
        self.osmosdr_source_0.set_center_freq(self.freq, 0)
        self.facsink_0.set_baseband_freq(self.freq)


def main(top_block_cls=top_block, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
