# Signal and Systems PBL Project - Multipath Channel Analysis

## Overview

This repository contains Python implementations for analyzing multipath effects in wireless communication systems as part of a Signal and Systems PBL project. The codebase demonstrates channel modeling, signal distortion analysis, and compensation techniques through Python simulations.

## Project Details

- **Core Tasks**:
  1. Multipath channel modeling using LTI systems
  2. Time-domain signal propagation simulation
  3. Frequency-domain distortion analysis
  4. Simplified channel equalizer design
- **Programming Language**: Python 3.10+

## Repository Purpose

The repository aims to:
1. Provide reference implementations for multipath channel modeling
2. Demonstrate signal distortion and compensation techniques
3. Share comparative analysis of time/frequency domain characteristics
4. Facilitate learning through practical examples of LTI system applications

## Getting Started
Before starting, make sure you have Python installed. I use Python 3.12, but it should work with Python 3.10+.

1. Clone this repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run the modules in the order described in the [Module explanation](#module-explanation) section for proper execution.

### Module explanation
1. `signal_sim.py`: BPSK signal generation and transmission simulation module implementing modulation, convolutional channel modeling, and signal visualization.
2. `channel_model.py`: Implements multipath channel modeling with configurable path gains and delays, generating impulse responses for wireless communication simulations.
3. `frequency_analysis.py`: Implements frequency-domain analysis comparing transmitted and received signal spectra using FFT techniques.
4. `equalize_and_snr.py`: Implements signal equalization and SNR calculation for received signals in multipath channels.

Note: `equalizer.py` and `utils.py` are modules and cannot be executed independently.

## Contributing
This repo might be inactive after the cource is finished, but contributions to this project are still welcome.

Please feel free to submit issues or pull requests to improve the code or documentation.

## License
MIT License. See [LICENSE](LICENSE) for more details.