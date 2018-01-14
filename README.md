# datadog-gpustat

[Agent Check](https://docs.datadoghq.com/agent/agent_checks/)
to get metrics from [NVIDIA Management Library (NVML)](https://developer.nvidia.com/nvidia-management-library-nvml)

![screenshot](screenshot.png)

## Installation

```sh
sudo -u dd-agent /opt/datadog-agent/embedded/bin/pip install -r requirements.txt
sudo -u dd-agent cp -a gpu_stat.py /etc/dd-agent/checks.d/
sudo -u dd-agent cp -a gpu_stat.yaml /etc/dd-agent/conf.d/
sudo systemctl restart datadog-agent
```

To test installation, run

```sh
sudo -u dd-agent dd-agent check gpu_stat
```

## Licence

The MIT License  
Copyright (c) 2018 Tsukasa OMOTO

## Acknowledgments

- [wookayin/gpustat](https://github.com/wookayin/gpustat)
  - [nvidia-ml-py](https://pypi.python.org/pypi/nvidia-ml-py/)
- [ngi644/datadog_nvml](https://github.com/ngi644/datadog_nvml)
