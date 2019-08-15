target = int(input('target 2018 = '))
achievement = int(input('achievement 2018 = '))

if achievement<target:
    new_target=target
elif achievement>=target:
    new_target=achievement+(target*.2)
print('target 2019 = ',new_target)