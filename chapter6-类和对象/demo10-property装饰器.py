class Cell:
    # 用 @property 修饰方法，相当于为该属性设置 getter 方法
    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        if 'alive' in value.lower():
            self._state = 'alive'
        else:
            self._state = 'dead'

    @property
    def is_dead(self):
        return not self._state.lower() == 'alive'


c = Cell()
c.state = 'Alive'
print(c.state)
print(c.is_dead)
