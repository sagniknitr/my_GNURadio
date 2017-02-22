#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Thu Dec  1 10:52:43 2016
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

from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.wxgui import fftsink2
from gnuradio.wxgui import forms
from gnuradio.wxgui import numbersink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import osmosdr
import time
import wx


class top_block(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Top Block")

        ##################################################
        # Variables
        ##################################################
        self.snr_vary = snr_vary = 1e-2
        self.samp_rate_0 = samp_rate_0 = 10e5
        self.samp_rate = samp_rate = 1e6
        self.channel_width = channel_width = 200e3
        self.center_freq = center_freq = 800e6

        ##################################################
        # Blocks
        ##################################################
        _center_freq_sizer = wx.BoxSizer(wx.VERTICAL)
        self._center_freq_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_center_freq_sizer,
        	value=self.center_freq,
        	callback=self.set_center_freq,
        	label='center_freq',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._center_freq_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_center_freq_sizer,
        	value=self.center_freq,
        	callback=self.set_center_freq,
        	minimum=750e6,
        	maximum=900e6,
        	num_steps=1000,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_center_freq_sizer)
        self.wxgui_numbersink2_0_0_0 = numbersink2.number_sink_f(
        	self.GetWin(),
        	unit="Units",
        	minval=-100,
        	maxval=100,
        	factor=1.0,
        	decimal_places=2,
        	ref_level=0,
        	sample_rate=samp_rate,
        	number_rate=15,
        	average=False,
        	avg_alpha=None,
        	label="energy2",
        	peak_hold=False,
        	show_gauge=True,
        )
        self.Add(self.wxgui_numbersink2_0_0_0.win)
        self.wxgui_numbersink2_0_0 = numbersink2.number_sink_f(
        	self.GetWin(),
        	unit="Units",
        	minval=-100,
        	maxval=100,
        	factor=1.0,
        	decimal_places=2,
        	ref_level=0,
        	sample_rate=samp_rate,
        	number_rate=15,
        	average=False,
        	avg_alpha=None,
        	label="energy_my",
        	peak_hold=False,
        	show_gauge=True,
        )
        self.Add(self.wxgui_numbersink2_0_0.win)
        self.wxgui_fftsink2_0 = fftsink2.fft_sink_c(
        	self.GetWin(),
        	baseband_freq=0,
        	y_per_div=10,
        	y_divs=10,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=samp_rate,
        	fft_size=1024,
        	fft_rate=15,
        	average=False,
        	avg_alpha=None,
        	title="FFT Plot",
        	peak_hold=False,
        )
        self.Add(self.wxgui_fftsink2_0.win)
        _snr_vary_sizer = wx.BoxSizer(wx.VERTICAL)
        self._snr_vary_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_snr_vary_sizer,
        	value=self.snr_vary,
        	callback=self.set_snr_vary,
        	label='snr_vary',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._snr_vary_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_snr_vary_sizer,
        	value=self.snr_vary,
        	callback=self.set_snr_vary,
        	minimum=0,
        	maximum=1,
        	num_steps=1000,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_snr_vary_sizer)
        self.osmosdr_source_0 = osmosdr.source( args="numchan=" + str(1) + " " + "" )
        self.osmosdr_source_0.set_sample_rate(samp_rate)
        self.osmosdr_source_0.set_center_freq(center_freq, 0)
        self.osmosdr_source_0.set_freq_corr(0, 0)
        self.osmosdr_source_0.set_dc_offset_mode(0, 0)
        self.osmosdr_source_0.set_iq_balance_mode(0, 0)
        self.osmosdr_source_0.set_gain_mode(False, 0)
        self.osmosdr_source_0.set_gain(0, 0)
        self.osmosdr_source_0.set_if_gain(20, 0)
        self.osmosdr_source_0.set_bb_gain(20, 0)
        self.osmosdr_source_0.set_antenna("", 0)
        self.osmosdr_source_0.set_bandwidth(0, 0)
          
        self.dc_blocker_xx_0 = filter.dc_blocker_cc(1024, True)
        self.blocks_nlog10_ff_0_0 = blocks.nlog10_ff(10, 1, 0)
        self.blocks_nlog10_ff_0 = blocks.nlog10_ff(10, 1, 0)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_moving_average_xx_0 = blocks.moving_average_ff(50000, 20e-6, 4000)
        self.blocks_file_sink_0_0 = blocks.file_sink(gr.sizeof_float*1, "/home/nitr/Dropbox/Sagnik_project/grc_files/bladeRF_data/signal_data_cyclo_50db_2.dat", False)
        self.blocks_file_sink_0_0.set_unbuffered(False)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_float*1, "/home/nitr/Dropbox/Sagnik_project/grc_files/bladeRF_data/signal_data_ED_50db.dat", False)
        self.blocks_file_sink_0.set_unbuffered(False)
        self.blocks_conjugate_cc_0 = blocks.conjugate_cc()
        self.blocks_complex_to_real_0_0 = blocks.complex_to_real(1)
        self.blocks_complex_to_real_0 = blocks.complex_to_real(1)
        self.blocks_complex_to_mag_squared_0 = blocks.complex_to_mag_squared(1)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_complex_to_mag_squared_0, 0), (self.blocks_nlog10_ff_0, 0))    
        self.connect((self.blocks_complex_to_real_0, 0), (self.blocks_moving_average_xx_0, 0))    
        self.connect((self.blocks_complex_to_real_0_0, 0), (self.blocks_file_sink_0_0, 0))    
        self.connect((self.blocks_conjugate_cc_0, 0), (self.blocks_multiply_xx_0, 0))    
        self.connect((self.blocks_moving_average_xx_0, 0), (self.blocks_nlog10_ff_0_0, 0))    
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_complex_to_real_0, 0))    
        self.connect((self.blocks_nlog10_ff_0, 0), (self.wxgui_numbersink2_0_0, 0))    
        self.connect((self.blocks_nlog10_ff_0_0, 0), (self.blocks_file_sink_0, 0))    
        self.connect((self.blocks_nlog10_ff_0_0, 0), (self.wxgui_numbersink2_0_0_0, 0))    
        self.connect((self.dc_blocker_xx_0, 0), (self.blocks_complex_to_mag_squared_0, 0))    
        self.connect((self.dc_blocker_xx_0, 0), (self.blocks_complex_to_real_0_0, 0))    
        self.connect((self.dc_blocker_xx_0, 0), (self.blocks_conjugate_cc_0, 0))    
        self.connect((self.dc_blocker_xx_0, 0), (self.blocks_multiply_xx_0, 1))    
        self.connect((self.dc_blocker_xx_0, 0), (self.wxgui_fftsink2_0, 0))    
        self.connect((self.osmosdr_source_0, 0), (self.dc_blocker_xx_0, 0))    

    def get_snr_vary(self):
        return self.snr_vary

    def set_snr_vary(self, snr_vary):
        self.snr_vary = snr_vary
        self._snr_vary_slider.set_value(self.snr_vary)
        self._snr_vary_text_box.set_value(self.snr_vary)

    def get_samp_rate_0(self):
        return self.samp_rate_0

    def set_samp_rate_0(self, samp_rate_0):
        self.samp_rate_0 = samp_rate_0

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.osmosdr_source_0.set_sample_rate(self.samp_rate)
        self.wxgui_fftsink2_0.set_sample_rate(self.samp_rate)

    def get_channel_width(self):
        return self.channel_width

    def set_channel_width(self, channel_width):
        self.channel_width = channel_width

    def get_center_freq(self):
        return self.center_freq

    def set_center_freq(self, center_freq):
        self.center_freq = center_freq
        self._center_freq_slider.set_value(self.center_freq)
        self._center_freq_text_box.set_value(self.center_freq)
        self.osmosdr_source_0.set_center_freq(self.center_freq, 0)


def main(top_block_cls=top_block, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
