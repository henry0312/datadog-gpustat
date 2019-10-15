# -*- coding: utf-8 -*-

# See:
#   - https://docs.datadoghq.com/developers/write_agent_check/

import time

import mock

# the following try/except block will make the custom check compatible with any Agent version
try:
    # first, try to import the base class from old versions of the Agent...
    from checks import AgentCheck
except ImportError:
    # ...if the above failed, the check is running in Agent version 6 or later
    from datadog_checks.checks import AgentCheck

# so dirty work-around for "error: setupterm: could not find terminal"
with mock.patch('blessings.Terminal'):
    from gpustat import GPUStatCollection

# content of the special variable __version__ will be shown in the Agent status page
__version__ = "1.0.0"


class GpuStat(AgentCheck):
    def check(self, instance):
        try:
            gpu_stats = GPUStatCollection.new_query()
            for gpu in gpu_stats.gpus:
                entry = gpu.entry
                tags = ['gpu:{}'.format(entry['index'])]
                self.gauge('gpu.memory.used', entry['memory.used'], tags=tags)
                self.gauge('gpu.memory.total', entry['memory.total'], tags=tags)
                self.gauge('gpu.utilization', entry['utilization.gpu'], tags=tags)
                self.gauge('gpu.temperature', entry['temperature.gpu'], tags=tags)
                self.gauge('gpu.power.draw', entry['power.draw'], tags=tags)
                self.gauge('gpu.enforced.power.limit', entry['enforced.power.limit'], tags=tags)
        except Exception as ex:
            self.event({
                'timestamp': int(time.time()),
                'event_type': 'gpu_stat',
                'msg_title': 'Error in gpu stat',
                'msg_text': str(ex),
            })
