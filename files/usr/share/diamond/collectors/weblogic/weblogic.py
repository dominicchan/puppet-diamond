import diamond.collector
import sys
import subprocess
import re
import string

class WeblogicCollector(diamond.collector.Collector):

    def get_default_config(self):
        """
        Returns the default collector settings
        """
        config = super(WeblogicCollector, self).get_default_config()
        config.update({
            'enabled':  False,
        })
        return config

    def collect(self):
        p = subprocess.Popen([self.config['wlstpath'], self.config['wlstscript']], env={'JAVA_HOME':self.config['java_home']}, stdout=subprocess.PIPE)
        for line in iter(p.stdout.readline,''):
            if re.match("^metric:", line) is not None:
                label, metric_name, shortname, metric_value = string.split(line.rstrip(),":")
                # Publish Metric
                self.publish(metric_name, metric_value)
