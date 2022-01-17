if self.level < 1:
	platform_group.empty() #сброс platform_group
	platforms.clear() #очистка листа
	pf_x = 0 ; pf_y = 0 #сброс pf_x, pf_y - позиций для инициализации
	platform_init(players[0].level) #цикл инициализации

pf_x = pf_y = 0
platforms = ["1"]

def platform_init(lvl): #функция инициализации платформ
	global pf_x, pf_y
	for line in levels_map[lvl]:
		for symbol in line:
			if symbol == "1":
				pf = Platform(pf_x, pf_y)
				platform_group.add(pf)
				platforms.append(pf)
			pf_x += platform_width
		pf_y += platform_height
		pf_x = 0

platform_init(players[0].level)
