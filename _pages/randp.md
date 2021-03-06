---
permalink: /randp/
title: "Research and Project"
gallery:
  - url: randp/algorithm.png
    image_path: randp/algorithm.png
    alt: "key bytes selection algorithm"
    title: "Key Bytes Selection Algorithm"
  - url: randp/res.png
    image_path: randp/res.png
    alt: "attention score result"
    title: "Attention Score Result"
---

My academic research falls into two main areas: network traffic measurement (including: encrypted traffic and malicious traffic) and blockchain-related studies. One strand of research in this first area explores how to design efficient and reliable traffic identification methods or frameworks for ISPs to ensure QoS while securing the network environment. My interest in designing deep learning models also informs projects.

# Network Traffic Measurement
  
## Tor-UP
![Language](https://img.shields.io/badge/language-python-brightgreen)
- An Unsupervised Pre-training  method for Obfuscated Tor Traffic.
  1. We deploy several Tor bridges with multiple pluggable transports and collected raw traffic. A dataset covering two mainstream obfuscation technologies and 24 applications is open-sourced.
  2. A novel traffic-oriented unsupervised pre-training task, Masked Byte Model is proposed. We design a pre-training model with three embeddings and the Transformer Encoder to extract generic traffic features.
  3. Tor-UP outperforms other methods and its accuracy exceeds 99% in all tasks.
  4. This work has been submitted to ***IEEE 2023 GlobeCom***.

## FastTraffic
![Language](https://img.shields.io/badge/language-python-brightgreen)
- An end-to-end lightweight approach for ubiquitous network management devices.
  1. Based on the IP packet structure, we propose and design an N-gram packet characterization model to achieve lightweight and efficient characterization of network traffic;
  2. Accurately classify VPN and Tor traffic, with 95% recognition accuracy and 1000 PPS throughput.
  3. This work has been submitted to ***Computer Networks***.

## GateKeeper
![Language](https://img.shields.io/badge/language-python-brightgreen)
- An end-to-end UltraLite approach for edge gateway devices.
  1. An interpretable fusion IP packet fixed transmission structure based on Self-attention mechanism is designed and proposed as a keyword node selection algorithm to achieve high optimization of model inputs; 
  2. Accurately classify VPN and Tor traffic with 91% accuracy and 300KB model size.
  3. This work conference version has been accepted by ***IEEE 2023 ICC***, and the journal version has been submitted to ***IEEE Internet of Things Journal***.

{% include gallery %}

  
