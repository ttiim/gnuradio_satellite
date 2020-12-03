#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Reaktor Hello World decoder
# Author: Daniel Estevez, Timothy Wriglesworth
# Description: Reaktor Hello World decoder
# GNU Radio version: 3.8.2.0

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

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from gnuradio import blocks
from gnuradio import digital
from gnuradio import filter
from gnuradio import gr
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio import zeromq
import pduadd
import satellites
import satellites.hier

from gnuradio import qtgui

class openlst_satellite(gr.top_block, Qt.QWidget):

    def __init__(self, invert=1, ip='127.0.0.1', port=7355):
        gr.top_block.__init__(self, "Reaktor Hello World decoder")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Reaktor Hello World decoder")
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

        self.settings = Qt.QSettings("GNU Radio", "openlst_satellite")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Parameters
        ##################################################
        self.invert = invert
        self.ip = ip
        self.port = port

        ##################################################
        # Variables
        ##################################################
        self.threshold = threshold = 1
        self.samp_rate = samp_rate = 48000
        self.preamble = preamble = "1010101010101010"
        self.gain_mu = gain_mu = 0.175*3
        self.access_code = access_code = "11010011100100011101001110010001"

        ##################################################
        # Blocks
        ##################################################
        self.zeromq_pub_msg_sink_0 = zeromq.pub_msg_sink('tcp://127.0.0.2:5559', 100, )
        self.satellites_sync_to_pdu_packed_0 = satellites.hier.sync_to_pdu_packed(
            packlen=255,
            sync=access_code,
            threshold=1,
        )
        self.satellites_print_timestamp_0 = satellites.print_timestamp('%Y-%m-%d %H:%M:%S', True)
        self.satellites_pn9_scrambler_0 = satellites.hier.pn9_scrambler()
        self.satellites_pdu_head_tail_1 = satellites.pdu_head_tail(3, 1)
        self.satellites_pdu_head_tail_0 = satellites.pdu_head_tail(1, 3)
        self.satellites_check_cc11xx_crc_0 = satellites.check_cc11xx_crc(True)
        self.satellites_cc11xx_packet_crop_0 = satellites.cc11xx_packet_crop(True)
        self.qtgui_time_sink_x_1 = qtgui.time_sink_f(
            3000, #size
            9600, #samp_rate
            'dots', #name
            1 #number of inputs
        )
        self.qtgui_time_sink_x_1.set_update_time(0.10)
        self.qtgui_time_sink_x_1.set_y_axis(-3, 3)

        self.qtgui_time_sink_x_1.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_1.enable_tags(True)
        self.qtgui_time_sink_x_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_1.enable_autoscale(False)
        self.qtgui_time_sink_x_1.enable_grid(False)
        self.qtgui_time_sink_x_1.enable_axis_labels(True)
        self.qtgui_time_sink_x_1.enable_control_panel(True)
        self.qtgui_time_sink_x_1.enable_stem_plot(False)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [0, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [0, -1, -1, -1, -1,
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
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_1_win)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
            30000, #size
            48000, #samp_rate
            "", #name
            1 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(True)
        self.qtgui_time_sink_x_0.enable_stem_plot(False)


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
                self.qtgui_time_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_win)
        self.pduadd_usrp_pad_0 = pduadd.usrp_pad(100, 1)
        self.pduadd_pdu_head_tail_1 = pduadd.pdu_head_tail(access_code)
        self.pduadd_pdu_head_tail_0 = pduadd.pdu_head_tail(preamble)
        self.pduadd_crc16_0 = pduadd.crc16()
        self.pduadd_add_length_0 = pduadd.add_length()
        self.low_pass_filter_0 = filter.fir_filter_fff(
            1,
            firdes.low_pass(
                1,
                48000,
                8000,
                600,
                firdes.WIN_HAMMING,
                6.76))
        self.digital_clock_recovery_mm_xx_0 = digital.clock_recovery_mm_ff(5, 0.25*gain_mu*gain_mu, 0.5, gain_mu, 0.005)
        self.digital_binary_slicer_fb_0 = digital.binary_slicer_fb()
        self.blocks_wavfile_source_0 = blocks.wavfile_source('/home/ethan/install/imit_tim/whitened_GFSK.wav', True)
        self.blocks_throttle_0_0 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_ff(invert)
        self.blocks_message_debug_0 = blocks.message_debug()



        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.pduadd_add_length_0, 'out'), (self.pduadd_crc16_0, 'in'))
        self.msg_connect((self.pduadd_crc16_0, 'out'), (self.satellites_check_cc11xx_crc_0, 'in'))
        self.msg_connect((self.pduadd_pdu_head_tail_0, 'out'), (self.pduadd_usrp_pad_0, 'in'))
        self.msg_connect((self.pduadd_pdu_head_tail_1, 'out'), (self.pduadd_pdu_head_tail_0, 'in'))
        self.msg_connect((self.pduadd_usrp_pad_0, 'out'), (self.satellites_print_timestamp_0, 'in'))
        self.msg_connect((self.satellites_cc11xx_packet_crop_0, 'out'), (self.satellites_pdu_head_tail_1, 'in'))
        self.msg_connect((self.satellites_check_cc11xx_crc_0, 'ok'), (self.pduadd_pdu_head_tail_1, 'in'))
        self.msg_connect((self.satellites_pdu_head_tail_0, 'out'), (self.pduadd_add_length_0, 'in'))
        self.msg_connect((self.satellites_pdu_head_tail_1, 'out'), (self.satellites_pdu_head_tail_0, 'in'))
        self.msg_connect((self.satellites_pn9_scrambler_0, 'out'), (self.satellites_cc11xx_packet_crop_0, 'in'))
        self.msg_connect((self.satellites_print_timestamp_0, 'out'), (self.blocks_message_debug_0, 'print_pdu'))
        self.msg_connect((self.satellites_print_timestamp_0, 'out'), (self.zeromq_pub_msg_sink_0, 'in'))
        self.msg_connect((self.satellites_sync_to_pdu_packed_0, 'out'), (self.satellites_pn9_scrambler_0, 'in'))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.blocks_throttle_0_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_throttle_0_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.blocks_wavfile_source_0, 0), (self.blocks_throttle_0_0, 0))
        self.connect((self.digital_binary_slicer_fb_0, 0), (self.satellites_sync_to_pdu_packed_0, 0))
        self.connect((self.digital_clock_recovery_mm_xx_0, 0), (self.digital_binary_slicer_fb_0, 0))
        self.connect((self.digital_clock_recovery_mm_xx_0, 0), (self.qtgui_time_sink_x_1, 0))
        self.connect((self.low_pass_filter_0, 0), (self.digital_clock_recovery_mm_xx_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "openlst_satellite")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_invert(self):
        return self.invert

    def set_invert(self, invert):
        self.invert = invert
        self.blocks_multiply_const_vxx_0.set_k(self.invert)

    def get_ip(self):
        return self.ip

    def set_ip(self, ip):
        self.ip = ip

    def get_port(self):
        return self.port

    def set_port(self, port):
        self.port = port

    def get_threshold(self):
        return self.threshold

    def set_threshold(self, threshold):
        self.threshold = threshold

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle_0_0.set_sample_rate(self.samp_rate)

    def get_preamble(self):
        return self.preamble

    def set_preamble(self, preamble):
        self.preamble = preamble

    def get_gain_mu(self):
        return self.gain_mu

    def set_gain_mu(self, gain_mu):
        self.gain_mu = gain_mu
        self.digital_clock_recovery_mm_xx_0.set_gain_omega(0.25*self.gain_mu*self.gain_mu)
        self.digital_clock_recovery_mm_xx_0.set_gain_mu(self.gain_mu)

    def get_access_code(self):
        return self.access_code

    def set_access_code(self, access_code):
        self.access_code = access_code
        self.satellites_sync_to_pdu_packed_0.set_sync(self.access_code)




def argument_parser():
    description = 'Reaktor Hello World decoder'
    parser = ArgumentParser(description=description)
    parser.add_argument(
        "-i", "--invert", dest="invert", type=intx, default=1,
        help="Set invert the waveform (-1 to invert) [default=%(default)r]")
    parser.add_argument(
        "--ip", dest="ip", type=str, default='127.0.0.1',
        help="Set UDP listen IP [default=%(default)r]")
    parser.add_argument(
        "--port", dest="port", type=intx, default=7355,
        help="Set UDP port [default=%(default)r]")
    return parser


def main(top_block_cls=openlst_satellite, options=None):
    if options is None:
        options = argument_parser().parse_args()

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls(invert=options.invert, ip=options.ip, port=options.port)

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    def quitting():
        tb.stop()
        tb.wait()

    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()

if __name__ == '__main__':
    main()
