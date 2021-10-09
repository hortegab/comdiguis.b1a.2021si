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
from b_FLL_tunner2 import b_FLL_tunner2  # grc-generated hier_block
from b_demod_constelacion_cb import b_demod_constelacion_cb  # grc-generated hier_block
from gnuradio import analog
from gnuradio import blocks
import numpy
from gnuradio import digital
from gnuradio import gr
from gnuradio.fft import window
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio.qtgui import Range, RangeWidget
from PyQt5 import QtCore
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
        self.samp_rate = samp_rate = 100e3
        self.const0 = const0 = digital.constellation_qpsk().points()
        self.Sps = Sps = 1
        self.run_stop = run_stop = True
        self.mapinverse = mapinverse = coding.inverse_map(const0)
        self.mapdirect = mapdirect = coding.direct_map(const0)
        self.f_d = f_d = 0
        self.Rs = Rs = samp_rate/Sps
        self.Noise = Noise = 0.1
        self.M0 = M0 = len(const0)

        ##################################################
        # Blocks
        ##################################################
        self._f_d_range = Range(0, 1400, 1400/100, 0, 200)
        self._f_d_win = RangeWidget(self._f_d_range, self.set_f_d, 'Desviacion de Frecuencia', "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_grid_layout.addWidget(self._f_d_win, 2, 0, 1, 1)
        for r in range(2, 3):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._Noise_range = Range(0, 10, 0.1, 0.1, 200)
        self._Noise_win = RangeWidget(self._Noise_range, self.set_Noise, 'Noise', "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_grid_layout.addWidget(self._Noise_win, 1, 0, 1, 1)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        _run_stop_check_box = Qt.QCheckBox('Inicial/Parar')
        self._run_stop_choices = {True: True, False: False}
        self._run_stop_choices_inv = dict((v,k) for k,v in self._run_stop_choices.items())
        self._run_stop_callback = lambda i: Qt.QMetaObject.invokeMethod(_run_stop_check_box, "setChecked", Qt.Q_ARG("bool", self._run_stop_choices_inv[i]))
        self._run_stop_callback(self.run_stop)
        _run_stop_check_box.stateChanged.connect(lambda i: self.set_run_stop(self._run_stop_choices[bool(i)]))
        self.top_grid_layout.addWidget(_run_stop_check_box, 0, 0, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_1_0 = qtgui.time_sink_f(
            1024, #size
            Rs, #samp_rate
            "", #name
            2, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_1_0.set_update_time(0.10)
        self.qtgui_time_sink_x_1_0.set_y_axis(-1, 9)

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
        self.qtgui_time_sink_x_1 = qtgui.time_sink_f(
            1024, #size
            Rs, #samp_rate
            "", #name
            2, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_1.set_update_time(0.10)
        self.qtgui_time_sink_x_1.set_y_axis(-1, 9)

        self.qtgui_time_sink_x_1.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_1.enable_tags(True)
        self.qtgui_time_sink_x_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_1.enable_autoscale(False)
        self.qtgui_time_sink_x_1.enable_grid(False)
        self.qtgui_time_sink_x_1.enable_axis_labels(True)
        self.qtgui_time_sink_x_1.enable_control_panel(False)
        self.qtgui_time_sink_x_1.enable_stem_plot(True)


        labels = ['T0', 'R0', 'Signal 3', 'Signal 4', 'Signal 5',
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
                self.qtgui_time_sink_x_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_1.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_1.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_1.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_1.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_1.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_1.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_1_win = sip.wrapinstance(self.qtgui_time_sink_x_1.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_1_win, 1, 1, 2, 2)
        for r in range(1, 3):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 3):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_const_sink_x_0 = qtgui.const_sink_c(
            1024, #size
            "", #name
            2, #number of inputs
            None # parent
        )
        self.qtgui_const_sink_x_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_0.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0.enable_grid(False)
        self.qtgui_const_sink_x_0.enable_axis_labels(True)


        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
            "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(2):
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
        self.digital_diff_encoder_bb_0 = digital.diff_encoder_bb(M0)
        self.digital_diff_decoder_bb_0 = digital.diff_decoder_bb(M0)
        self.digital_chunks_to_symbols_xx_1 = digital.chunks_to_symbols_bc(const0, 1)
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_char*1)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_char_to_float_0_1 = blocks.char_to_float(1, 1)
        self.blocks_char_to_float_0_0_0 = blocks.char_to_float(1, 1)
        self.blocks_char_to_float_0_0 = blocks.char_to_float(1, 1)
        self.blocks_char_to_float_0 = blocks.char_to_float(1, 1)
        self.blocks_add_xx_0 = blocks.add_vcc(1)
        self.b_demod_constelacion_cb_0 = b_demod_constelacion_cb(
            Constelacion=const0,
        )
        self.b_FLL_tunner2_0 = b_FLL_tunner2(
            Constellation=const0,
        )
        self.analog_sig_source_x_1 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, f_d, 1, 0, 0)
        self.analog_random_source_x_1 = blocks.vector_source_b(list(map(int, numpy.random.randint(0, M0, 10000000))), True)
        self.analog_noise_source_x_0 = analog.noise_source_c(analog.GR_GAUSSIAN, Noise, 0)
        self.analog_const_source_x_0 = analog.sig_source_c(0, analog.GR_CONST_WAVE, 0, 0, np.exp(math.pi*1j))



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_const_source_x_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.analog_noise_source_x_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.analog_random_source_x_1, 0), (self.blocks_char_to_float_0_1, 0))
        self.connect((self.analog_random_source_x_1, 0), (self.digital_diff_encoder_bb_0, 0))
        self.connect((self.analog_sig_source_x_1, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.b_FLL_tunner2_0, 0), (self.b_demod_constelacion_cb_0, 0))
        self.connect((self.b_FLL_tunner2_0, 0), (self.qtgui_const_sink_x_0, 1))
        self.connect((self.b_demod_constelacion_cb_0, 0), (self.blocks_char_to_float_0_0, 0))
        self.connect((self.b_demod_constelacion_cb_0, 0), (self.digital_map_bb_0_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_multiply_xx_0, 2))
        self.connect((self.blocks_char_to_float_0, 0), (self.qtgui_time_sink_x_1, 0))
        self.connect((self.blocks_char_to_float_0_0, 0), (self.qtgui_time_sink_x_1, 1))
        self.connect((self.blocks_char_to_float_0_0_0, 0), (self.qtgui_time_sink_x_1_0, 1))
        self.connect((self.blocks_char_to_float_0_1, 0), (self.qtgui_time_sink_x_1_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.b_FLL_tunner2_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.qtgui_const_sink_x_0, 0))
        self.connect((self.digital_chunks_to_symbols_xx_1, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.digital_diff_decoder_bb_0, 0), (self.blocks_char_to_float_0_0_0, 0))
        self.connect((self.digital_diff_decoder_bb_0, 0), (self.blocks_null_sink_0, 0))
        self.connect((self.digital_diff_encoder_bb_0, 0), (self.digital_map_bb_0, 0))
        self.connect((self.digital_map_bb_0, 0), (self.blocks_char_to_float_0, 0))
        self.connect((self.digital_map_bb_0, 0), (self.digital_chunks_to_symbols_xx_1, 0))
        self.connect((self.digital_map_bb_0_0, 0), (self.digital_diff_decoder_bb_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "ser_simulation")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_Rs(self.samp_rate/self.Sps)
        self.analog_sig_source_x_1.set_sampling_freq(self.samp_rate)

    def get_const0(self):
        return self.const0

    def set_const0(self, const0):
        self.const0 = const0
        self.set_M0(len(self.const0))
        self.set_mapdirect(coding.direct_map(self.const0))
        self.set_mapinverse(coding.inverse_map(self.const0))
        self.b_FLL_tunner2_0.set_Constellation(self.const0)
        self.b_demod_constelacion_cb_0.set_Constelacion(self.const0)
        self.digital_chunks_to_symbols_xx_1.set_symbol_table(self.const0)

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

    def get_Rs(self):
        return self.Rs

    def set_Rs(self, Rs):
        self.Rs = Rs
        self.qtgui_time_sink_x_1.set_samp_rate(self.Rs)
        self.qtgui_time_sink_x_1_0.set_samp_rate(self.Rs)

    def get_Noise(self):
        return self.Noise

    def set_Noise(self, Noise):
        self.Noise = Noise
        self.analog_noise_source_x_0.set_amplitude(self.Noise)

    def get_M0(self):
        return self.M0

    def set_M0(self, M0):
        self.M0 = M0




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
