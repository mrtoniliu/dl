import adv_test
import adv
from adv import *
from module import energy

def module():
    return Lucretia

class Lucretia(adv.Adv):
    a3 = ('bk',0.3)
     
    def init(this):
        if this.condition('energy'):
            this.prerun = this.c_prerun

    def prerun(this):
        energy.Energy(this,
                self={} ,
                team={} 
                )
        Event('energized').listener(this.energy_doublebuff)

    def c_prerun(this):
        energy.Energy(this,
                self={'s1':1,'s2':2} ,
                team={'s1':1}
                )
        Event('energized').listener(this.energy_doublebuff)

    def energy_doublebuff(this, e):
        adv.Selfbuff("double_buff", 0.2, 15).on()



from slot.a import *
if __name__ == '__main__':
    conf = {}
    #conf['slot.a'] = RR()+CE()
    conf['acl'] = """
        `s2, seq=5 and cancel
        `s3, sx=2 
        `s1, sx=3
        `s1, seq=5 and cancel
        """

    if 1:
        conf['acl'] = """
            `s1, seq=5 and cancel
            `s2, seq=5 and cancel
            `s3, seq=5 and cancel
            """

    adv_test.test(module(), conf, verbose=0)



'''
2 1 | 2 3 1 | 2 1 | 1 3 2 | 2 1 | 3 2 1 | 2 1 | 2 3 1 | 2 1 | 2 3 1 |
2 3 | 5 0 1 | 3 4 | 5 0 2 | 4 5 | 0 2 3 | 5 0.| 2 2 3 | 5 0 | 2 2 3 |

2 1 | 2 1 3 | 2 1 | 2 1 3 | 
2 3 | 5 0 0 | 2 3 | 5 0 0 |

2 1 | 2 3 1 | 2 1 | 2 3 1 | 
2 3 | 5 0 1 | 3 4 | 6.0 1 |

2 1 | 2 3 1 | 2 1 | 1 3 2 | 2 1 | 3 2 1 | 1 2 | 3 2 1
2 3 | 5 0 1 | 3 4 | 5 0 2 | 4 5 | 0 2 3 | 4 6.| 0 2 3
'''
