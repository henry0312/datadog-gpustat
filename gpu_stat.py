# -*- coding: utf-8 -*-

# See:
#   - https://docs.datadoghq.com/agent/agent_checks/
#   - https://docs.datadoghq.com/ja/guides/agent_checks/

import time

from checks import AgentCheck
from gpustat import GPUStatCollection


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
