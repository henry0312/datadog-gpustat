SHELL := /bin/bash

install:
	@sudo -u dd-agent /opt/datadog-agent/embedded/bin/pip install -r requirements.txt
	@sudo -u dd-agent cp -a gpu_stat.py /etc/dd-agent/checks.d/
	@sudo -u dd-agent cp -a gpu_stat.yaml /etc/dd-agent/conf.d/
	@sudo systemctl restart datadog-agent
.PHONY: install

uninstall:
	@sudo -u dd-agent rm /etc/dd-agent/checks.d/gpu_stat.py
	@sudo -u dd-agent rm /etc/dd-agent/conf.d/gpu_stat.yaml
	@sudo systemctl restart datadog-agent
.PHONY: uninstall

check:
	@sudo -u dd-agent dd-agent check gpu_stat
.PHONY: check
