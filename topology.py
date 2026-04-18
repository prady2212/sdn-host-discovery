from mininet.net import Mininet
from mininet.node import RemoteController, OVSSwitch
from mininet.topo import Topo
from mininet.log import setLogLevel
from mininet.cli import CLI

class CustomTopo(Topo):
    def build(self):
        s1 = self.addSwitch('s1')
        h1 = self.addHost('h1', ip='10.0.0.1/24')
        h2 = self.addHost('h2', ip='10.0.0.2/24')
        h3 = self.addHost('h3', ip='10.0.0.3/24')
        self.addLink(h1, s1)
        self.addLink(h2, s1)
        self.addLink(h3, s1)

if __name__ == '__main__':
    setLogLevel('info')
    topo = CustomTopo()
    net = Mininet(topo=topo,
                  controller=RemoteController('c0', ip='127.0.0.1', port=6633),
                  switch=OVSSwitch)
    net.start()
    CLI(net)
    net.stop()
