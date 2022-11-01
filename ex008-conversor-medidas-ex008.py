d = float(input('Digite uma distância em metros: '))
km = d/1000
hm = d/100
dam = d/10
dm = d*10
cm = d*100
mm = d*1000
print('A medida em {:.0f}m corresponde à {:.0f}cm, {:.0f}mm, {}km , {}hm , {}dam , {}dm'.format(d, cm, mm, km, hm, dam, dm))
