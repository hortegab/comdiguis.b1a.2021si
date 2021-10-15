#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: SER Simulation
# Author: Homero Ortega Boada
# Description: Dale un valor a Es/No, corre el flujograma y obten la SER. Puedes sacar tantos valores como para construir una curva de SER
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
from b_Manual_Equalizer_cc import b_Manual_Equalizer_cc  # grc-generated hier_block
from b_demod_constelacion_cb import b_demod_constelacion_cb  # grc-generated hier_block
from gnuradio import analog
from gnuradio import blocks
import numpy
from gnuradio import channels
from gnuradio import digital
from gnuradio import gr
from gnuradio.fft import window
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio.qtgui import Range, RangeWidget
from PyQt5 import QtCore
from scipy import fftpack
import coding  # embedded python module
import math
import numpy as np



from gnuradio import qtgui

class ser_simulation(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "SER Simulation", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("SER Simulation")
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

        self.settings = Qt.QSettings("GNU Radio", "ser_simulation")

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
        self.tap7 = tap7 = 1
        self.tap6 = tap6 = 1
        self.tap5 = tap5 = 1
        self.tap4 = tap4 = 1
        self.tap3 = tap3 = 1
        self.tap2 = tap2 = 1
        self.tap1 = tap1 = 1
        self.tap0 = tap0 = 1
        self.samp_rate = samp_rate = 100e3
        self.e_tap7 = e_tap7 = 1
        self.e_tap6 = e_tap6 = 1
        self.e_tap5 = e_tap5 = 1
        self.e_tap4 = e_tap4 = 1
        self.e_tap3 = e_tap3 = 1
        self.e_tap2 = e_tap2 = 1
        self.e_tap1 = e_tap1 = 1
        self.e_tap0 = e_tap0 = 1
        self.constel = constel = digital.constellation_qpsk().points()
        self.Sps = Sps = 1
        self.run_stop = run_stop = True
        self.phase_d = phase_d = 0
        self.mapinverse = mapinverse = coding.inverse_map(constel)
        self.mapdirect = mapdirect = coding.direct_map(constel)
        self.f_d = f_d = 0
        self.eq_gain = eq_gain = 0.01
        self.a_d = a_d = 1
        self.Rs = Rs = samp_rate/Sps
        self.Retardo_sym = Retardo_sym = 2
        self.Noise = Noise = 0.1
        self.M = M = len(constel)
        self.Jitter = Jitter = 0
        self.Eq_taps = Eq_taps = fftpack.ifftshift(fftpack.ifft([e_tap0, e_tap1, e_tap2, e_tap3, e_tap4, e_tap5, e_tap6, e_tap7]))
        self.Dtiming = Dtiming = 0
        self.Ch_taps = Ch_taps = fftpack.ifftshift(fftpack.ifft([tap0, tap1, tap2, tap3, tap4, tap5, tap6, tap7]))

        ##################################################
        # Blocks
        ##################################################
        self.controles = Qt.QTabWidget()
        self.controles_widget_0 = Qt.QWidget()
        self.controles_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.controles_widget_0)
        self.controles_grid_layout_0 = Qt.QGridLayout()
        self.controles_layout_0.addLayout(self.controles_grid_layout_0)
        self.controles.addTab(self.controles_widget_0, 'El canal y Soluciones a Efectos del Canal')
        self.top_grid_layout.addWidget(self.controles, 1, 0, 1, 1)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.ManSol = Qt.QTabWidget()
        self.ManSol_widget_0 = Qt.QWidget()
        self.ManSol_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.ManSol_widget_0)
        self.ManSol_grid_layout_0 = Qt.QGridLayout()
        self.ManSol_layout_0.addLayout(self.ManSol_grid_layout_0)
        self.ManSol.addTab(self.ManSol_widget_0, 'Solutions Testing')
        self.ManSol_widget_1 = Qt.QWidget()
        self.ManSol_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.ManSol_widget_1)
        self.ManSol_grid_layout_1 = Qt.QGridLayout()
        self.ManSol_layout_1.addLayout(self.ManSol_grid_layout_1)
        self.ManSol.addTab(self.ManSol_widget_1, 'Manual Equalizer Solution Control')
        self.controles_grid_layout_0.addWidget(self.ManSol, 3, 0, 1, 1)
        for r in range(3, 4):
            self.controles_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 1):
            self.controles_grid_layout_0.setColumnStretch(c, 1)
        self.ChBeh = Qt.QTabWidget()
        self.ChBeh_widget_0 = Qt.QWidget()
        self.ChBeh_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.ChBeh_widget_0)
        self.ChBeh_grid_layout_0 = Qt.QGridLayout()
        self.ChBeh_layout_0.addLayout(self.ChBeh_grid_layout_0)
        self.ChBeh.addTab(self.ChBeh_widget_0, 'Channel Parameters')
        self.ChBeh_widget_1 = Qt.QWidget()
        self.ChBeh_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.ChBeh_widget_1)
        self.ChBeh_grid_layout_1 = Qt.QGridLayout()
        self.ChBeh_layout_1.addLayout(self.ChBeh_grid_layout_1)
        self.ChBeh.addTab(self.ChBeh_widget_1, 'Channel Nonlinearities')
        self.controles_grid_layout_0.addWidget(self.ChBeh, 1, 0, 1, 1)
        for r in range(1, 2):
            self.controles_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 1):
            self.controles_grid_layout_0.setColumnStretch(c, 1)
        self._phase_d_range = Range(-math.pi, math.pi, 2*math.pi/100, 0, 200)
        self._phase_d_win = RangeWidget(self._phase_d_range, self.set_phase_d, 'Phase Deviatio', "counter_slider", float, QtCore.Qt.Horizontal)
        self.ChBeh_grid_layout_0.addWidget(self._phase_d_win, 1, 0, 1, 1)
        for r in range(1, 2):
            self.ChBeh_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 1):
            self.ChBeh_grid_layout_0.setColumnStretch(c, 1)
        self._f_d_range = Range(0, 1400, 1400/100, 0, 200)
        self._f_d_win = RangeWidget(self._f_d_range, self.set_f_d, 'Frequency Deviation', "counter_slider", float, QtCore.Qt.Horizontal)
        self.ChBeh_grid_layout_0.addWidget(self._f_d_win, 2, 0, 1, 1)
        for r in range(2, 3):
            self.ChBeh_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 1):
            self.ChBeh_grid_layout_0.setColumnStretch(c, 1)
        self._e_tap7_range = Range(0, 3, 0.01, 1, 200)
        self._e_tap7_win = RangeWidget(self._e_tap7_range, self.set_e_tap7, 'Sub Band -1', "counter_slider", float, QtCore.Qt.Horizontal)
        self.ManSol_grid_layout_1.addWidget(self._e_tap7_win, 3, 0, 1, 1)
        for r in range(3, 4):
            self.ManSol_grid_layout_1.setRowStretch(r, 1)
        for c in range(0, 1):
            self.ManSol_grid_layout_1.setColumnStretch(c, 1)
        self._e_tap6_range = Range(0, 3, 0.01, 1, 200)
        self._e_tap6_win = RangeWidget(self._e_tap6_range, self.set_e_tap6, 'Sub Band -2', "counter_slider", float, QtCore.Qt.Horizontal)
        self.ManSol_grid_layout_1.addWidget(self._e_tap6_win, 2, 0, 1, 1)
        for r in range(2, 3):
            self.ManSol_grid_layout_1.setRowStretch(r, 1)
        for c in range(0, 1):
            self.ManSol_grid_layout_1.setColumnStretch(c, 1)
        self._e_tap5_range = Range(0, 3, 0.01, 1, 200)
        self._e_tap5_win = RangeWidget(self._e_tap5_range, self.set_e_tap5, 'Sub Band -3', "counter_slider", float, QtCore.Qt.Horizontal)
        self.ManSol_grid_layout_1.addWidget(self._e_tap5_win, 1, 0, 1, 1)
        for r in range(1, 2):
            self.ManSol_grid_layout_1.setRowStretch(r, 1)
        for c in range(0, 1):
            self.ManSol_grid_layout_1.setColumnStretch(c, 1)
        self._e_tap4_range = Range(0, 3, 0.01, 1, 200)
        self._e_tap4_win = RangeWidget(self._e_tap4_range, self.set_e_tap4, 'Sub Band -4,4', "counter_slider", float, QtCore.Qt.Horizontal)
        self.ManSol_grid_layout_1.addWidget(self._e_tap4_win, 0, 0, 1, 1)
        for r in range(0, 1):
            self.ManSol_grid_layout_1.setRowStretch(r, 1)
        for c in range(0, 1):
            self.ManSol_grid_layout_1.setColumnStretch(c, 1)
        self._e_tap3_range = Range(0, 3, 0.01, 1, 200)
        self._e_tap3_win = RangeWidget(self._e_tap3_range, self.set_e_tap3, 'Sub Band 3', "counter_slider", float, QtCore.Qt.Horizontal)
        self.ManSol_grid_layout_1.addWidget(self._e_tap3_win, 8, 0, 1, 1)
        for r in range(8, 9):
            self.ManSol_grid_layout_1.setRowStretch(r, 1)
        for c in range(0, 1):
            self.ManSol_grid_layout_1.setColumnStretch(c, 1)
        self._e_tap2_range = Range(0, 3, 0.01, 1, 200)
        self._e_tap2_win = RangeWidget(self._e_tap2_range, self.set_e_tap2, 'Sub Band 2', "counter_slider", float, QtCore.Qt.Horizontal)
        self.ManSol_grid_layout_1.addWidget(self._e_tap2_win, 6, 0, 1, 1)
        for r in range(6, 7):
            self.ManSol_grid_layout_1.setRowStretch(r, 1)
        for c in range(0, 1):
            self.ManSol_grid_layout_1.setColumnStretch(c, 1)
        self._e_tap1_range = Range(0, 3, 0.01, 1, 200)
        self._e_tap1_win = RangeWidget(self._e_tap1_range, self.set_e_tap1, 'Sub Band 1', "counter_slider", float, QtCore.Qt.Horizontal)
        self.ManSol_grid_layout_1.addWidget(self._e_tap1_win, 5, 0, 1, 1)
        for r in range(5, 6):
            self.ManSol_grid_layout_1.setRowStretch(r, 1)
        for c in range(0, 1):
            self.ManSol_grid_layout_1.setColumnStretch(c, 1)
        self._e_tap0_range = Range(0, 3, 0.01, 1, 200)
        self._e_tap0_win = RangeWidget(self._e_tap0_range, self.set_e_tap0, 'Sub Band 0', "counter_slider", float, QtCore.Qt.Horizontal)
        self.ManSol_grid_layout_1.addWidget(self._e_tap0_win, 4, 0, 1, 1)
        for r in range(4, 5):
            self.ManSol_grid_layout_1.setRowStretch(r, 1)
        for c in range(0, 1):
            self.ManSol_grid_layout_1.setColumnStretch(c, 1)
        self._a_d_range = Range(0, 1, 1/100, 1, 200)
        self._a_d_win = RangeWidget(self._a_d_range, self.set_a_d, 'Fading', "counter_slider", float, QtCore.Qt.Horizontal)
        self.ChBeh_grid_layout_0.addWidget(self._a_d_win, 3, 0, 1, 1)
        for r in range(3, 4):
            self.ChBeh_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 1):
            self.ChBeh_grid_layout_0.setColumnStretch(c, 1)
        self._Retardo_sym_range = Range(0, Sps*10, 1, 2, 200)
        self._Retardo_sym_win = RangeWidget(self._Retardo_sym_range, self.set_Retardo_sym, 'Delay transmited signal to match with the received signal', "counter_slider", int, QtCore.Qt.Horizontal)
        self.ManSol_grid_layout_0.addWidget(self._Retardo_sym_win, 0, 0, 1, 1)
        for r in range(0, 1):
            self.ManSol_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 1):
            self.ManSol_grid_layout_0.setColumnStretch(c, 1)
        self._Noise_range = Range(0, 10, 0.1, 0.1, 200)
        self._Noise_win = RangeWidget(self._Noise_range, self.set_Noise, 'Noise', "counter_slider", float, QtCore.Qt.Horizontal)
        self.ChBeh_grid_layout_0.addWidget(self._Noise_win, 0, 0, 1, 1)
        for r in range(0, 1):
            self.ChBeh_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 1):
            self.ChBeh_grid_layout_0.setColumnStretch(c, 1)
        self._tap7_range = Range(0, 3, 0.01, 1, 200)
        self._tap7_win = RangeWidget(self._tap7_range, self.set_tap7, 'Sub Band -1', "counter_slider", float, QtCore.Qt.Horizontal)
        self.ChBeh_grid_layout_1.addWidget(self._tap7_win, 3, 0, 1, 1)
        for r in range(3, 4):
            self.ChBeh_grid_layout_1.setRowStretch(r, 1)
        for c in range(0, 1):
            self.ChBeh_grid_layout_1.setColumnStretch(c, 1)
        self._tap6_range = Range(0, 3, 0.01, 1, 200)
        self._tap6_win = RangeWidget(self._tap6_range, self.set_tap6, 'Sub Band -2', "counter_slider", float, QtCore.Qt.Horizontal)
        self.ChBeh_grid_layout_1.addWidget(self._tap6_win, 2, 0, 1, 1)
        for r in range(2, 3):
            self.ChBeh_grid_layout_1.setRowStretch(r, 1)
        for c in range(0, 1):
            self.ChBeh_grid_layout_1.setColumnStretch(c, 1)
        self._tap5_range = Range(0, 3, 0.01, 1, 200)
        self._tap5_win = RangeWidget(self._tap5_range, self.set_tap5, 'Sub Band -3', "counter_slider", float, QtCore.Qt.Horizontal)
        self.ChBeh_grid_layout_1.addWidget(self._tap5_win, 1, 0, 1, 1)
        for r in range(1, 2):
            self.ChBeh_grid_layout_1.setRowStretch(r, 1)
        for c in range(0, 1):
            self.ChBeh_grid_layout_1.setColumnStretch(c, 1)
        self._tap4_range = Range(0, 3, 0.01, 1, 200)
        self._tap4_win = RangeWidget(self._tap4_range, self.set_tap4, 'Sub Band -4,4', "counter_slider", float, QtCore.Qt.Horizontal)
        self.ChBeh_grid_layout_1.addWidget(self._tap4_win, 0, 0, 1, 1)
        for r in range(0, 1):
            self.ChBeh_grid_layout_1.setRowStretch(r, 1)
        for c in range(0, 1):
            self.ChBeh_grid_layout_1.setColumnStretch(c, 1)
        self._tap3_range = Range(0, 3, 0.01, 1, 200)
        self._tap3_win = RangeWidget(self._tap3_range, self.set_tap3, 'Sub Band 3', "counter_slider", float, QtCore.Qt.Horizontal)
        self.ChBeh_grid_layout_1.addWidget(self._tap3_win, 8, 0, 1, 1)
        for r in range(8, 9):
            self.ChBeh_grid_layout_1.setRowStretch(r, 1)
        for c in range(0, 1):
            self.ChBeh_grid_layout_1.setColumnStretch(c, 1)
        self._tap2_range = Range(0, 3, 0.01, 1, 200)
        self._tap2_win = RangeWidget(self._tap2_range, self.set_tap2, 'Sub Band 2', "counter_slider", float, QtCore.Qt.Horizontal)
        self.ChBeh_grid_layout_1.addWidget(self._tap2_win, 6, 0, 1, 1)
        for r in range(6, 7):
            self.ChBeh_grid_layout_1.setRowStretch(r, 1)
        for c in range(0, 1):
            self.ChBeh_grid_layout_1.setColumnStretch(c, 1)
        self._tap1_range = Range(0, 3, 0.01, 1, 200)
        self._tap1_win = RangeWidget(self._tap1_range, self.set_tap1, 'Sub Band 1', "counter_slider", float, QtCore.Qt.Horizontal)
        self.ChBeh_grid_layout_1.addWidget(self._tap1_win, 5, 0, 1, 1)
        for r in range(5, 6):
            self.ChBeh_grid_layout_1.setRowStretch(r, 1)
        for c in range(0, 1):
            self.ChBeh_grid_layout_1.setColumnStretch(c, 1)
        self._tap0_range = Range(0, 3, 0.01, 1, 200)
        self._tap0_win = RangeWidget(self._tap0_range, self.set_tap0, 'Sub Band 0', "counter_slider", float, QtCore.Qt.Horizontal)
        self.ChBeh_grid_layout_1.addWidget(self._tap0_win, 4, 0, 1, 1)
        for r in range(4, 5):
            self.ChBeh_grid_layout_1.setRowStretch(r, 1)
        for c in range(0, 1):
            self.ChBeh_grid_layout_1.setColumnStretch(c, 1)
        _run_stop_check_box = Qt.QCheckBox('Inicial/Parar')
        self._run_stop_choices = {True: True, False: False}
        self._run_stop_choices_inv = dict((v,k) for k,v in self._run_stop_choices.items())
        self._run_stop_callback = lambda i: Qt.QMetaObject.invokeMethod(_run_stop_check_box, "setChecked", Qt.Q_ARG("bool", self._run_stop_choices_inv[i]))
        self._run_stop_callback(self.run_stop)
        _run_stop_check_box.stateChanged.connect(lambda i: self.set_run_stop(self._run_stop_choices[bool(i)]))
        self.controles_grid_layout_0.addWidget(_run_stop_check_box, 0, 0, 1, 1)
        for r in range(0, 1):
            self.controles_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 1):
            self.controles_grid_layout_0.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_1_0 = qtgui.time_sink_f(
            1024, #size
            Rs, #samp_rate
            "", #name
            2, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_1_0.set_update_time(0.10)
        self.qtgui_time_sink_x_1_0.set_y_axis(-1, M)

        self.qtgui_time_sink_x_1_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_1_0.enable_tags(True)
        self.qtgui_time_sink_x_1_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_1_0.enable_autoscale(False)
        self.qtgui_time_sink_x_1_0.enable_grid(False)
        self.qtgui_time_sink_x_1_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_1_0.enable_control_panel(False)
        self.qtgui_time_sink_x_1_0.enable_stem_plot(True)


        labels = ['T-1', 'R-1', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [0, 0, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(2):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_1_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_1_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_1_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_1_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_1_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_1_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_1_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_1_0_win = sip.wrapinstance(self.qtgui_time_sink_x_1_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_1_0_win, 7, 1, 1, 2)
        for r in range(7, 8):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 3):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_freq_sink_x_0_1 = qtgui.freq_sink_c(
            1024, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            Rs, #bw
            '', #name
            3,
            None # parent
        )
        self.qtgui_freq_sink_x_0_1.set_update_time(0.10)
        self.qtgui_freq_sink_x_0_1.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0_1.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_1.enable_autoscale(False)
        self.qtgui_freq_sink_x_0_1.enable_grid(False)
        self.qtgui_freq_sink_x_0_1.set_fft_average(0.05)
        self.qtgui_freq_sink_x_0_1.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_1.enable_control_panel(False)
        self.qtgui_freq_sink_x_0_1.set_fft_window_normalized(False)



        labels = ['Entrada del Canal', 'Salida del canal', 'Salida del Ecualizador', '', '',
            '', '', '', '', '']
        widths = [2, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(3):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_1.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_1.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_1.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_1.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_1_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_1.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_1_win, 1, 1, 1, 2)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 3):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_const_sink_x_0 = qtgui.const_sink_c(
            1024, #size
            "", #name
            3, #number of inputs
            None # parent
        )
        self.qtgui_const_sink_x_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_0.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0.enable_grid(False)
        self.qtgui_const_sink_x_0.enable_axis_labels(True)


        labels = ['Entrada del Canal', 'Salida del Canal', 'Salida del Ecualizador', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "red", "red",
            "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(3):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_const_sink_x_0_win, 7, 0, 1, 1)
        for r in range(7, 8):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.digital_map_bb_0_0 = digital.map_bb(mapinverse)
        self.digital_map_bb_0 = digital.map_bb(mapdirect)
        self.digital_diff_encoder_bb_0 = digital.diff_encoder_bb(M)
        self.digital_diff_decoder_bb_0 = digital.diff_decoder_bb(M)
        self.digital_chunks_to_symbols_xx_1 = digital.chunks_to_symbols_bc(constel, 1)
        self.channels_channel_model_0 = channels.channel_model(
            noise_voltage=0,
            frequency_offset=0,
            epsilon=1.,
            taps=Ch_taps,
            noise_seed=13,
            block_tags=False)
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_char*1)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_cc(0.5)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_cc(a_d)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_float*1, Retardo_sym)
        self.blocks_char_to_float_0_1 = blocks.char_to_float(1, 1)
        self.blocks_char_to_float_0_0_0 = blocks.char_to_float(1, 1)
        self.blocks_add_xx_0 = blocks.add_vcc(1)
        self.b_demod_constelacion_cb_0 = b_demod_constelacion_cb(
            Constelacion=constel,
        )
        self.b_Manual_Equalizer_cc_0 = b_Manual_Equalizer_cc(
            taps=[e_tap0,e_tap1,e_tap2,e_tap3,e_tap4,e_tap5,e_tap6,e_tap7],
        )
        self.analog_sig_source_x_1 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, f_d, 1, 0, 0)
        self.analog_random_source_x_1 = blocks.vector_source_b(list(map(int, numpy.random.randint(0, M, 10000000))), True)
        self.analog_noise_source_x_0 = analog.noise_source_c(analog.GR_GAUSSIAN, Noise, 0)
        self.analog_const_source_x_0 = analog.sig_source_c(0, analog.GR_CONST_WAVE, 0, 0, np.exp(phase_d*1j))
        self._Jitter_range = Range(0, Sps, 1, 0, 200)
        self._Jitter_win = RangeWidget(self._Jitter_range, self.set_Jitter, 'Jitter', "counter_slider", int, QtCore.Qt.Horizontal)
        self.ChBeh_grid_layout_0.addWidget(self._Jitter_win, 4, 0, 1, 1)
        for r in range(4, 5):
            self.ChBeh_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 1):
            self.ChBeh_grid_layout_0.setColumnStretch(c, 1)
        self._Dtiming_range = Range(0, Sps-1, 1, 0, 200)
        self._Dtiming_win = RangeWidget(self._Dtiming_range, self.set_Dtiming, 'Timing', "counter_slider", int, QtCore.Qt.Horizontal)
        self.ManSol_grid_layout_0.addWidget(self._Dtiming_win, 1, 0, 1, 1)
        for r in range(1, 2):
            self.ManSol_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 1):
            self.ManSol_grid_layout_0.setColumnStretch(c, 1)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_const_source_x_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.analog_noise_source_x_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.analog_random_source_x_1, 0), (self.blocks_char_to_float_0_1, 0))
        self.connect((self.analog_random_source_x_1, 0), (self.digital_diff_encoder_bb_0, 0))
        self.connect((self.analog_sig_source_x_1, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.b_Manual_Equalizer_cc_0, 0), (self.b_demod_constelacion_cb_0, 0))
        self.connect((self.b_Manual_Equalizer_cc_0, 0), (self.qtgui_const_sink_x_0, 2))
        self.connect((self.b_Manual_Equalizer_cc_0, 0), (self.qtgui_freq_sink_x_0_1, 2))
        self.connect((self.b_demod_constelacion_cb_0, 0), (self.digital_map_bb_0_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_multiply_xx_0, 2))
        self.connect((self.blocks_char_to_float_0_0_0, 0), (self.qtgui_time_sink_x_1_0, 1))
        self.connect((self.blocks_char_to_float_0_1, 0), (self.blocks_delay_0, 0))
        self.connect((self.blocks_delay_0, 0), (self.qtgui_time_sink_x_1_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.channels_channel_model_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.qtgui_const_sink_x_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.qtgui_freq_sink_x_0_1, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.b_Manual_Equalizer_cc_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.qtgui_const_sink_x_0, 1))
        self.connect((self.blocks_multiply_xx_0, 0), (self.qtgui_freq_sink_x_0_1, 1))
        self.connect((self.channels_channel_model_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.digital_chunks_to_symbols_xx_1, 0), (self.blocks_multiply_const_vxx_0_0, 0))
        self.connect((self.digital_diff_decoder_bb_0, 0), (self.blocks_char_to_float_0_0_0, 0))
        self.connect((self.digital_diff_decoder_bb_0, 0), (self.blocks_null_sink_0, 0))
        self.connect((self.digital_diff_encoder_bb_0, 0), (self.digital_map_bb_0, 0))
        self.connect((self.digital_map_bb_0, 0), (self.digital_chunks_to_symbols_xx_1, 0))
        self.connect((self.digital_map_bb_0_0, 0), (self.digital_diff_decoder_bb_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "ser_simulation")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_tap7(self):
        return self.tap7

    def set_tap7(self, tap7):
        self.tap7 = tap7
        self.set_Ch_taps(fftpack.ifftshift(fftpack.ifft([self.tap0, self.tap1, self.tap2, self.tap3, self.tap4, self.tap5, self.tap6, self.tap7])))

    def get_tap6(self):
        return self.tap6

    def set_tap6(self, tap6):
        self.tap6 = tap6
        self.set_Ch_taps(fftpack.ifftshift(fftpack.ifft([self.tap0, self.tap1, self.tap2, self.tap3, self.tap4, self.tap5, self.tap6, self.tap7])))

    def get_tap5(self):
        return self.tap5

    def set_tap5(self, tap5):
        self.tap5 = tap5
        self.set_Ch_taps(fftpack.ifftshift(fftpack.ifft([self.tap0, self.tap1, self.tap2, self.tap3, self.tap4, self.tap5, self.tap6, self.tap7])))

    def get_tap4(self):
        return self.tap4

    def set_tap4(self, tap4):
        self.tap4 = tap4
        self.set_Ch_taps(fftpack.ifftshift(fftpack.ifft([self.tap0, self.tap1, self.tap2, self.tap3, self.tap4, self.tap5, self.tap6, self.tap7])))

    def get_tap3(self):
        return self.tap3

    def set_tap3(self, tap3):
        self.tap3 = tap3
        self.set_Ch_taps(fftpack.ifftshift(fftpack.ifft([self.tap0, self.tap1, self.tap2, self.tap3, self.tap4, self.tap5, self.tap6, self.tap7])))

    def get_tap2(self):
        return self.tap2

    def set_tap2(self, tap2):
        self.tap2 = tap2
        self.set_Ch_taps(fftpack.ifftshift(fftpack.ifft([self.tap0, self.tap1, self.tap2, self.tap3, self.tap4, self.tap5, self.tap6, self.tap7])))

    def get_tap1(self):
        return self.tap1

    def set_tap1(self, tap1):
        self.tap1 = tap1
        self.set_Ch_taps(fftpack.ifftshift(fftpack.ifft([self.tap0, self.tap1, self.tap2, self.tap3, self.tap4, self.tap5, self.tap6, self.tap7])))

    def get_tap0(self):
        return self.tap0

    def set_tap0(self, tap0):
        self.tap0 = tap0
        self.set_Ch_taps(fftpack.ifftshift(fftpack.ifft([self.tap0, self.tap1, self.tap2, self.tap3, self.tap4, self.tap5, self.tap6, self.tap7])))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_Rs(self.samp_rate/self.Sps)
        self.analog_sig_source_x_1.set_sampling_freq(self.samp_rate)

    def get_e_tap7(self):
        return self.e_tap7

    def set_e_tap7(self, e_tap7):
        self.e_tap7 = e_tap7
        self.set_Eq_taps(fftpack.ifftshift(fftpack.ifft([self.e_tap0, self.e_tap1, self.e_tap2, self.e_tap3, self.e_tap4, self.e_tap5, self.e_tap6, self.e_tap7])))
        self.b_Manual_Equalizer_cc_0.set_taps([self.e_tap0,self.e_tap1,self.e_tap2,self.e_tap3,self.e_tap4,self.e_tap5,self.e_tap6,self.e_tap7])

    def get_e_tap6(self):
        return self.e_tap6

    def set_e_tap6(self, e_tap6):
        self.e_tap6 = e_tap6
        self.set_Eq_taps(fftpack.ifftshift(fftpack.ifft([self.e_tap0, self.e_tap1, self.e_tap2, self.e_tap3, self.e_tap4, self.e_tap5, self.e_tap6, self.e_tap7])))
        self.b_Manual_Equalizer_cc_0.set_taps([self.e_tap0,self.e_tap1,self.e_tap2,self.e_tap3,self.e_tap4,self.e_tap5,self.e_tap6,self.e_tap7])

    def get_e_tap5(self):
        return self.e_tap5

    def set_e_tap5(self, e_tap5):
        self.e_tap5 = e_tap5
        self.set_Eq_taps(fftpack.ifftshift(fftpack.ifft([self.e_tap0, self.e_tap1, self.e_tap2, self.e_tap3, self.e_tap4, self.e_tap5, self.e_tap6, self.e_tap7])))
        self.b_Manual_Equalizer_cc_0.set_taps([self.e_tap0,self.e_tap1,self.e_tap2,self.e_tap3,self.e_tap4,self.e_tap5,self.e_tap6,self.e_tap7])

    def get_e_tap4(self):
        return self.e_tap4

    def set_e_tap4(self, e_tap4):
        self.e_tap4 = e_tap4
        self.set_Eq_taps(fftpack.ifftshift(fftpack.ifft([self.e_tap0, self.e_tap1, self.e_tap2, self.e_tap3, self.e_tap4, self.e_tap5, self.e_tap6, self.e_tap7])))
        self.b_Manual_Equalizer_cc_0.set_taps([self.e_tap0,self.e_tap1,self.e_tap2,self.e_tap3,self.e_tap4,self.e_tap5,self.e_tap6,self.e_tap7])

    def get_e_tap3(self):
        return self.e_tap3

    def set_e_tap3(self, e_tap3):
        self.e_tap3 = e_tap3
        self.set_Eq_taps(fftpack.ifftshift(fftpack.ifft([self.e_tap0, self.e_tap1, self.e_tap2, self.e_tap3, self.e_tap4, self.e_tap5, self.e_tap6, self.e_tap7])))
        self.b_Manual_Equalizer_cc_0.set_taps([self.e_tap0,self.e_tap1,self.e_tap2,self.e_tap3,self.e_tap4,self.e_tap5,self.e_tap6,self.e_tap7])

    def get_e_tap2(self):
        return self.e_tap2

    def set_e_tap2(self, e_tap2):
        self.e_tap2 = e_tap2
        self.set_Eq_taps(fftpack.ifftshift(fftpack.ifft([self.e_tap0, self.e_tap1, self.e_tap2, self.e_tap3, self.e_tap4, self.e_tap5, self.e_tap6, self.e_tap7])))
        self.b_Manual_Equalizer_cc_0.set_taps([self.e_tap0,self.e_tap1,self.e_tap2,self.e_tap3,self.e_tap4,self.e_tap5,self.e_tap6,self.e_tap7])

    def get_e_tap1(self):
        return self.e_tap1

    def set_e_tap1(self, e_tap1):
        self.e_tap1 = e_tap1
        self.set_Eq_taps(fftpack.ifftshift(fftpack.ifft([self.e_tap0, self.e_tap1, self.e_tap2, self.e_tap3, self.e_tap4, self.e_tap5, self.e_tap6, self.e_tap7])))
        self.b_Manual_Equalizer_cc_0.set_taps([self.e_tap0,self.e_tap1,self.e_tap2,self.e_tap3,self.e_tap4,self.e_tap5,self.e_tap6,self.e_tap7])

    def get_e_tap0(self):
        return self.e_tap0

    def set_e_tap0(self, e_tap0):
        self.e_tap0 = e_tap0
        self.set_Eq_taps(fftpack.ifftshift(fftpack.ifft([self.e_tap0, self.e_tap1, self.e_tap2, self.e_tap3, self.e_tap4, self.e_tap5, self.e_tap6, self.e_tap7])))
        self.b_Manual_Equalizer_cc_0.set_taps([self.e_tap0,self.e_tap1,self.e_tap2,self.e_tap3,self.e_tap4,self.e_tap5,self.e_tap6,self.e_tap7])

    def get_constel(self):
        return self.constel

    def set_constel(self, constel):
        self.constel = constel
        self.set_M(len(self.constel))
        self.set_mapdirect(coding.direct_map(self.constel))
        self.set_mapinverse(coding.inverse_map(self.constel))
        self.b_demod_constelacion_cb_0.set_Constelacion(self.constel)
        self.digital_chunks_to_symbols_xx_1.set_symbol_table(self.constel)

    def get_Sps(self):
        return self.Sps

    def set_Sps(self, Sps):
        self.Sps = Sps
        self.set_Rs(self.samp_rate/self.Sps)

    def get_run_stop(self):
        return self.run_stop

    def set_run_stop(self, run_stop):
        self.run_stop = run_stop
        if self.run_stop: self.start()
        else: self.stop(); self.wait()
        self._run_stop_callback(self.run_stop)

    def get_phase_d(self):
        return self.phase_d

    def set_phase_d(self, phase_d):
        self.phase_d = phase_d
        self.analog_const_source_x_0.set_offset(np.exp(self.phase_d*1j))

    def get_mapinverse(self):
        return self.mapinverse

    def set_mapinverse(self, mapinverse):
        self.mapinverse = mapinverse

    def get_mapdirect(self):
        return self.mapdirect

    def set_mapdirect(self, mapdirect):
        self.mapdirect = mapdirect

    def get_f_d(self):
        return self.f_d

    def set_f_d(self, f_d):
        self.f_d = f_d
        self.analog_sig_source_x_1.set_frequency(self.f_d)

    def get_eq_gain(self):
        return self.eq_gain

    def set_eq_gain(self, eq_gain):
        self.eq_gain = eq_gain

    def get_a_d(self):
        return self.a_d

    def set_a_d(self, a_d):
        self.a_d = a_d
        self.blocks_multiply_const_vxx_0.set_k(self.a_d)

    def get_Rs(self):
        return self.Rs

    def set_Rs(self, Rs):
        self.Rs = Rs
        self.qtgui_freq_sink_x_0_1.set_frequency_range(0, self.Rs)
        self.qtgui_time_sink_x_1_0.set_samp_rate(self.Rs)

    def get_Retardo_sym(self):
        return self.Retardo_sym

    def set_Retardo_sym(self, Retardo_sym):
        self.Retardo_sym = Retardo_sym
        self.blocks_delay_0.set_dly(self.Retardo_sym)

    def get_Noise(self):
        return self.Noise

    def set_Noise(self, Noise):
        self.Noise = Noise
        self.analog_noise_source_x_0.set_amplitude(self.Noise)

    def get_M(self):
        return self.M

    def set_M(self, M):
        self.M = M
        self.qtgui_time_sink_x_1_0.set_y_axis(-1, self.M)

    def get_Jitter(self):
        return self.Jitter

    def set_Jitter(self, Jitter):
        self.Jitter = Jitter

    def get_Eq_taps(self):
        return self.Eq_taps

    def set_Eq_taps(self, Eq_taps):
        self.Eq_taps = Eq_taps

    def get_Dtiming(self):
        return self.Dtiming

    def set_Dtiming(self, Dtiming):
        self.Dtiming = Dtiming

    def get_Ch_taps(self):
        return self.Ch_taps

    def set_Ch_taps(self, Ch_taps):
        self.Ch_taps = Ch_taps
        self.channels_channel_model_0.set_taps(self.Ch_taps)




def main(top_block_cls=ser_simulation, options=None):

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
