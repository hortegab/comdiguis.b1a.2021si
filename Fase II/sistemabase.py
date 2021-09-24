#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: sistemabase
# Author: homero
# GNU Radio version: 3.9.0.0

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

import os
import sys
sys.path.append(os.environ.get('GRC_HIER_PATH', os.path.expanduser('~/.grc_gnuradio')))

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from b_u_M_PAM_bb import b_u_M_PAM_bb  # grc-generated hier_block
from b_upconverter_cf import b_upconverter_cf  # grc-generated hier_block
from gnuradio import analog
from gnuradio import blocks
import numpy
from gnuradio import filter
from gnuradio import gr
from gnuradio.fft import window
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio.qtgui import Range, RangeWidget
from PyQt5 import QtCore
import epy_block_0_0
import math
import mis_funciones  # embedded python module
import numpy as np



from gnuradio import qtgui

class sistemabase(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "sistemabase", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("sistemabase")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "sistemabase")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.M = M = 8
        self.bps = bps = math.log(M,2)
        self.Rb = Rb = 32000
        self.Rs = Rs = Rb/bps
        self.fd = fd = 2*Rs
        self.Kf = Kf = fd/Rs
        self.Sps = Sps = int(16*Kf*M)
        self.samp_rate = samp_rate = Rs*Sps
        self.h0 = h0 = ([1]*Sps)
        self.Retardo_sym = Retardo_sym = 0
        self.Noise = Noise = 0.2
        self.Fc = Fc = fd*8
        self.Dtiming = Dtiming = 0

        ##################################################
        # Blocks
        ##################################################
        self._Noise_range = Range(0, 4, 0.1, 0.2, 200)
        self._Noise_win = RangeWidget(self._Noise_range, self.set_Noise, 'Noise', "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_grid_layout.addWidget(self._Noise_win, 2, 0, 1, 1)
        for r in range(2, 3):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.Menu = Qt.QTabWidget()
        self.Menu_widget_0 = Qt.QWidget()
        self.Menu_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.Menu_widget_0)
        self.Menu_grid_layout_0 = Qt.QGridLayout()
        self.Menu_layout_0.addLayout(self.Menu_grid_layout_0)
        self.Menu.addTab(self.Menu_widget_0, 'T1 R1')
        self.Menu_widget_1 = Qt.QWidget()
        self.Menu_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.Menu_widget_1)
        self.Menu_grid_layout_1 = Qt.QGridLayout()
        self.Menu_layout_1.addLayout(self.Menu_grid_layout_1)
        self.Menu.addTab(self.Menu_widget_1, 'T2 R2')
        self.Menu_widget_2 = Qt.QWidget()
        self.Menu_layout_2 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.Menu_widget_2)
        self.Menu_grid_layout_2 = Qt.QGridLayout()
        self.Menu_layout_2.addLayout(self.Menu_grid_layout_2)
        self.Menu.addTab(self.Menu_widget_2, 'T3 R3')
        self.Menu_widget_3 = Qt.QWidget()
        self.Menu_layout_3 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.Menu_widget_3)
        self.Menu_grid_layout_3 = Qt.QGridLayout()
        self.Menu_layout_3.addLayout(self.Menu_grid_layout_3)
        self.Menu.addTab(self.Menu_widget_3, 'Eye Diagramm')
        self.Menu_widget_4 = Qt.QWidget()
        self.Menu_layout_4 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.Menu_widget_4)
        self.Menu_grid_layout_4 = Qt.QGridLayout()
        self.Menu_layout_4.addLayout(self.Menu_grid_layout_4)
        self.Menu.addTab(self.Menu_widget_4, 'Timing')
        self.Menu_widget_5 = Qt.QWidget()
        self.Menu_layout_5 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.Menu_widget_5)
        self.Menu_grid_layout_5 = Qt.QGridLayout()
        self.Menu_layout_5.addLayout(self.Menu_grid_layout_5)
        self.Menu.addTab(self.Menu_widget_5, 'RF')
        self.Menu_widget_6 = Qt.QWidget()
        self.Menu_layout_6 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.Menu_widget_6)
        self.Menu_grid_layout_6 = Qt.QGridLayout()
        self.Menu_layout_6.addLayout(self.Menu_grid_layout_6)
        self.Menu.addTab(self.Menu_widget_6, 'constelaciones')
        self.top_grid_layout.addWidget(self.Menu, 4, 0, 1, 1)
        for r in range(4, 5):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_1 = qtgui.time_sink_f(
            int(Sps*18), #size
            samp_rate, #samp_rate
            "Senal RF", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_1.set_update_time(0.10)
        self.qtgui_time_sink_x_1.set_y_axis(-2, 2)

        self.qtgui_time_sink_x_1.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_1.enable_tags(True)
        self.qtgui_time_sink_x_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_1.enable_autoscale(False)
        self.qtgui_time_sink_x_1.enable_grid(False)
        self.qtgui_time_sink_x_1.enable_axis_labels(True)
        self.qtgui_time_sink_x_1.enable_control_panel(False)
        self.qtgui_time_sink_x_1.enable_stem_plot(False)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_1.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_1.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_1.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_1.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_1.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_1.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_1_win = sip.wrapinstance(self.qtgui_time_sink_x_1.pyqwidget(), Qt.QWidget)
        self.Menu_grid_layout_5.addWidget(self._qtgui_time_sink_x_1_win, 0, 0, 1, 1)
        for r in range(0, 1):
            self.Menu_grid_layout_5.setRowStretch(r, 1)
        for c in range(0, 1):
            self.Menu_grid_layout_5.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_0_0 = qtgui.time_sink_c(
            6*Sps, #size
            samp_rate, #samp_rate
            "", #name
            2, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0.set_y_axis(-2, 2)

        self.qtgui_time_sink_x_0_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_0.enable_tags(True)
        self.qtgui_time_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0_0.enable_stem_plot(False)


        labels = ['I signal Tx', 'Q Signal Tx', 'I signal Rx', 'Q signal Rx', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [2, 2, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(4):
            if len(labels[i]) == 0:
                if (i % 2 == 0):
                    self.qtgui_time_sink_x_0_0.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_0_0.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.Menu_grid_layout_1.addWidget(self._qtgui_time_sink_x_0_0_win, 0, 0, 1, 1)
        for r in range(0, 1):
            self.Menu_grid_layout_1.setRowStretch(r, 1)
        for c in range(0, 1):
            self.Menu_grid_layout_1.setColumnStretch(c, 1)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
            1024*8+8, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "Espectro en dB", #name
            2,
            None # parent
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(0.05)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)
        self.qtgui_freq_sink_x_0.set_fft_window_normalized(False)



        labels = ['T2', 'R2', '', '', '',
            '', '', '', '', '']
        widths = [3, 3, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(2):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.Menu_grid_layout_1.addWidget(self._qtgui_freq_sink_x_0_win, 1, 0, 1, 1)
        for r in range(1, 2):
            self.Menu_grid_layout_1.setRowStretch(r, 1)
        for c in range(0, 1):
            self.Menu_grid_layout_1.setColumnStretch(c, 1)
        self.qtgui_eye_sink_x_0 = qtgui.eye_sink_c(
            1024, #size
            samp_rate, #samp_rate
            1, #number of inputs
            None
        )
        self.qtgui_eye_sink_x_0.set_update_time(0.10)
        self.qtgui_eye_sink_x_0.set_samp_per_symbol(Sps)
        self.qtgui_eye_sink_x_0.set_y_axis(-6, 6)

        self.qtgui_eye_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_eye_sink_x_0.enable_tags(True)
        self.qtgui_eye_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_eye_sink_x_0.enable_autoscale(False)
        self.qtgui_eye_sink_x_0.enable_grid(False)
        self.qtgui_eye_sink_x_0.enable_axis_labels(True)
        self.qtgui_eye_sink_x_0.enable_control_panel(False)


        labels = ['R2', 'R2.0', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [4, 4, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'blue', 'blue', 'blue', 'blue',
            'blue', 'blue', 'blue', 'blue', 'blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(2):
            if len(labels[i]) == 0:
                if (i % 2 == 0):
                    self.qtgui_eye_sink_x_0.set_line_label(i, "Eye [Re{{Data {0}}}]".format(round(i/2)))
                else:
                    self.qtgui_eye_sink_x_0.set_line_label(i, "Eye [Im{{Data {0}}}]".format(round((i-1)/2)))
            else:
                self.qtgui_eye_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_eye_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_eye_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_eye_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_eye_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_eye_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_eye_sink_x_0_win = sip.wrapinstance(self.qtgui_eye_sink_x_0.pyqwidget(), Qt.QWidget)
        self.Menu_grid_layout_3.addWidget(self._qtgui_eye_sink_x_0_win, 0, 0, 1, 1)
        for r in range(0, 1):
            self.Menu_grid_layout_3.setRowStretch(r, 1)
        for c in range(0, 1):
            self.Menu_grid_layout_3.setColumnStretch(c, 1)
        self.qtgui_const_sink_x_0_0 = qtgui.const_sink_c(
            1024, #size
            "", #name
            2, #number of inputs
            None # parent
        )
        self.qtgui_const_sink_x_0_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0_0.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_0_0.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0_0.enable_grid(False)
        self.qtgui_const_sink_x_0_0.enable_axis_labels(True)


        labels = ['T2', 'R2', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
            "red", "red", "red", "red", "red"]
        styles = [1, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        markers = [-1, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(2):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.Menu_grid_layout_6.addWidget(self._qtgui_const_sink_x_0_0_win, 0, 1, 1, 1)
        for r in range(0, 1):
            self.Menu_grid_layout_6.setRowStretch(r, 1)
        for c in range(1, 2):
            self.Menu_grid_layout_6.setColumnStretch(c, 1)
        self.interp_fir_filter_xxx_0 = filter.interp_fir_filter_fff(Sps, h0)
        self.interp_fir_filter_xxx_0.declare_sample_delay(0)
        self.epy_block_0_0 = epy_block_0_0.blk(samp_rate=samp_rate)
        self.blocks_multiply_const_vxx_1 = blocks.multiply_const_ff(2*fd)
        self.blocks_char_to_float_1 = blocks.char_to_float(1, 1)
        self.blocks_add_xx_1 = blocks.add_vff(1)
        self.blocks_add_xx_0 = blocks.add_vcc(1)
        self.b_upconverter_cf_0 = b_upconverter_cf(
            Fc=Fc,
            samp_rate=samp_rate,
        )
        self.b_u_M_PAM_bb_0 = b_u_M_PAM_bb(
            M=M,
        )
        self.analog_random_source_x_0 = blocks.vector_source_b(list(map(int, numpy.random.randint(0, 2, 1000000))), True)
        self.analog_noise_source_x_0 = analog.noise_source_c(analog.GR_GAUSSIAN, Noise, 0)
        self.analog_const_source_x_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, -(M-1)/2)
        self._Retardo_sym_range = Range(0, Sps*10, 1, 0, 200)
        self._Retardo_sym_win = RangeWidget(self._Retardo_sym_range, self.set_Retardo_sym, 'Delay transmited signal to match with the received signal', "counter_slider", int, QtCore.Qt.Horizontal)
        self.top_grid_layout.addWidget(self._Retardo_sym_win, 1, 0, 1, 1)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._Dtiming_range = Range(0, Sps-1, 1, 0, 200)
        self._Dtiming_win = RangeWidget(self._Dtiming_range, self.set_Dtiming, 'Dtiming', "counter_slider", int, QtCore.Qt.Horizontal)
        self.top_grid_layout.addWidget(self._Dtiming_win, 0, 0, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_const_source_x_0, 0), (self.blocks_add_xx_1, 1))
        self.connect((self.analog_noise_source_x_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.analog_random_source_x_0, 0), (self.b_u_M_PAM_bb_0, 0))
        self.connect((self.b_u_M_PAM_bb_0, 0), (self.blocks_char_to_float_1, 0))
        self.connect((self.b_upconverter_cf_0, 0), (self.qtgui_time_sink_x_1, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.qtgui_const_sink_x_0_0, 1))
        self.connect((self.blocks_add_xx_0, 0), (self.qtgui_eye_sink_x_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.qtgui_freq_sink_x_0, 1))
        self.connect((self.blocks_add_xx_0, 0), (self.qtgui_time_sink_x_0_0, 1))
        self.connect((self.blocks_add_xx_1, 0), (self.blocks_multiply_const_vxx_1, 0))
        self.connect((self.blocks_char_to_float_1, 0), (self.blocks_add_xx_1, 0))
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.interp_fir_filter_xxx_0, 0))
        self.connect((self.epy_block_0_0, 0), (self.b_upconverter_cf_0, 0))
        self.connect((self.epy_block_0_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.epy_block_0_0, 0), (self.qtgui_const_sink_x_0_0, 0))
        self.connect((self.epy_block_0_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.epy_block_0_0, 0), (self.qtgui_time_sink_x_0_0, 0))
        self.connect((self.interp_fir_filter_xxx_0, 0), (self.epy_block_0_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "sistemabase")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_M(self):
        return self.M

    def set_M(self, M):
        self.M = M
        self.set_Sps(int(16*self.Kf*self.M))
        self.set_bps(math.log(self.M,2))
        self.analog_const_source_x_0.set_offset(-(self.M-1)/2)
        self.b_u_M_PAM_bb_0.set_M(self.M)

    def get_bps(self):
        return self.bps

    def set_bps(self, bps):
        self.bps = bps
        self.set_Rs(self.Rb/self.bps)

    def get_Rb(self):
        return self.Rb

    def set_Rb(self, Rb):
        self.Rb = Rb
        self.set_Rs(self.Rb/self.bps)

    def get_Rs(self):
        return self.Rs

    def set_Rs(self, Rs):
        self.Rs = Rs
        self.set_Kf(self.fd/self.Rs)
        self.set_fd(2*self.Rs)
        self.set_samp_rate(self.Rs*self.Sps)

    def get_fd(self):
        return self.fd

    def set_fd(self, fd):
        self.fd = fd
        self.set_Fc(self.fd*8)
        self.set_Kf(self.fd/self.Rs)
        self.blocks_multiply_const_vxx_1.set_k(2*self.fd)

    def get_Kf(self):
        return self.Kf

    def set_Kf(self, Kf):
        self.Kf = Kf
        self.set_Sps(int(16*self.Kf*self.M))

    def get_Sps(self):
        return self.Sps

    def set_Sps(self, Sps):
        self.Sps = Sps
        self.set_h0(([1]*self.Sps))
        self.set_samp_rate(self.Rs*self.Sps)
        self.qtgui_eye_sink_x_0.set_samp_per_symbol(self.Sps)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.b_upconverter_cf_0.set_samp_rate(self.samp_rate)
        self.epy_block_0_0.samp_rate = self.samp_rate
        self.qtgui_eye_sink_x_0.set_samp_rate(self.samp_rate)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_time_sink_x_0_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_1.set_samp_rate(self.samp_rate)

    def get_h0(self):
        return self.h0

    def set_h0(self, h0):
        self.h0 = h0
        self.interp_fir_filter_xxx_0.set_taps(self.h0)

    def get_Retardo_sym(self):
        return self.Retardo_sym

    def set_Retardo_sym(self, Retardo_sym):
        self.Retardo_sym = Retardo_sym

    def get_Noise(self):
        return self.Noise

    def set_Noise(self, Noise):
        self.Noise = Noise
        self.analog_noise_source_x_0.set_amplitude(self.Noise)

    def get_Fc(self):
        return self.Fc

    def set_Fc(self, Fc):
        self.Fc = Fc
        self.b_upconverter_cf_0.set_Fc(self.Fc)

    def get_Dtiming(self):
        return self.Dtiming

    def set_Dtiming(self, Dtiming):
        self.Dtiming = Dtiming




def main(top_block_cls=sistemabase, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
