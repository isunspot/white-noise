#!/usr/bin/env python

import os

import noise


class BrownNoise(noise.Noise):
    def play_noise(self, wave_out):
        my_dir = os.path.dirname(__file__)
        path = os.path.join(my_dir, 'brown-noise.wav')
        self.loop_file(wave_out, path)


if __name__ == '__main__':
    BrownNoise().run()
