from robobrowser import RoboBrowser

# Browse to a page with checkbox inputs
browser = RoboBrowser()

# browser = RoboBrowser(history=True)
browser.open('http://listado.tumoto.com.co/motos/')
makers = browser.select('#id_9991763-AMCO_1763_2 .qcat-truncate')

makers_index = range(0, len(makers))
for i in makers_index:
    browser.follow_link(makers[i])
    bikes = browser.select('.list-view-item-title a')
    bikes_index = range(0, len(bikes))

    anchor = browser.find_all(class_="ch-pagination-current").next_sibling

    for j in bikes_index:
        browser.follow_link(bikes[j])

        techs = browser.find_all(class_='tit')
        for tech in techs:
            if tech.text == 'Cilindrada (cc):':
                cc = tech.next.next.next.text
            elif tech.text == 'Color:':
                color = tech.next.next.next.text
            elif tech.text == 'Recorrido:':
                mileage = tech.next.next.next.text
            elif tech.text == 'Modelo:':
                model = tech.next.next.next.text
            elif tech.text == 'Marca:':
                maker = tech.next.next.next.text
            elif tech.text == 'Tipo:':
                type = tech.next.next.next.text

        name = browser.find('h1').text
        price = browser.find(class_='ch-price ch-price principal').text
        price = price.replace('\t', '').replace('$', '').replace('.', '')
        location = browser.find(class_='ubic').text
        year = browser.find_all(class_="atrDest")[0].text
        kms = browser.find_all(class_="atrDest")[1].text
        kms = kms.replace('|', '').replace('km', '').strip()
        url = browser.url
        img = browser.find(class_="first-img").attrs['data-src-original']

