import cocos
from Objects import label

class CombatText(cocos.layer.Layer):
    def __init__(self):
        self.kills = 0

        super(CombatText, self).__init__()
        self.health_label = label.labelClass('HP Remaining: ', False, 20)
        self.health_label.position = 120,\
                                     cocos.director.director.get_window_size()[1] - 50

        self.health_amount = label.labelClass('100', False, 20)
        self.health_amount.position = 230,\
                                     cocos.director.director.get_window_size()[1] - 50

        self.kills_label = label.labelClass('Kills: ', False, 20)
        self.kills_label.position = cocos.director.director.get_window_size()[0] - 100,\
                                    cocos.director.director.get_window_size()[1] - 50

        self.kills_amount = label.labelClass(str(self.kills), False, 20)
        self.kills_amount.position = cocos.director.director.get_window_size()[0] - 50,\
                                     cocos.director.director.get_window_size()[1] - 50

        self.add(self.health_label)
        self.add(self.health_amount)
        self.add(self.kills_label)
        self.add(self.kills_amount)

    def updateHP(self, newHealth):
        self.health_amount.element.text = '%s' % newHealth

    def incrementKills(self, newKills):
        self.kills_amount.element.text = '%s' % newKills