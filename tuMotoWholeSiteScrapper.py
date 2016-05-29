from robobrowser import RoboBrowser
import csv

# Browse to a page with checkbox inputs
browser = RoboBrowser()
# browser = RoboBrowser(history=True)
browser.open('http://listado.tumoto.com.co/motos/')

makers = browser.select('#id_9991763-AMCO_1763_2 .qcat-truncate')
for i in range(0, len(makers)):
    browser.follow_link(makers[i])

    bikes = browser.select('.list-view-item-title a')
    bikes_index = range(0, len(bikes))

    while len(bikes_index) > 0:
        next_page = browser.find_all('a', class_="prefetch")
        for j in bikes_index:
            browser.follow_link(bikes[j])
            techs = browser.find_all(class_='tit')
            for tech in techs:
                if tech.text == 'Cilindrada (cc):':
                    cc = tech.next.next.next.text
                elif tech.text == 'Recorrido:':
                    mileage = tech.next.next.next.text
                elif tech.text == 'Modelo:':
                    model = tech.next.next.next.text
                elif tech.text == 'Color:':
                    color = tech.next.next.next.text
                elif tech.text == 'Marca:':
                    maker = tech.next.next.next.text
                elif tech.text == 'Tipo:':
                    type = tech.next.next.next.text
            link = browser.url
            title = browser.find('h1').text
            location = browser.find(class_='ubic').text
            year = browser.find_all(class_="atrDest")[0].text
            img = browser.find(class_="src-delay-initiation").attrs['data-src-original']
            kms = browser.find_all(class_="atrDest")[1].text.replace('|', '').replace('km', '').strip()
            price = browser.find(class_='ch-price').text.replace('\t', '').replace('$', '').replace('.', '')

            with open('all_motos.csv', 'a', newline='') as csvfile:
                csv_writer = csv.writer(csvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                csv_writer.writerow([model, kms, img, title, link, price, year, maker])
            print("{};{};{};{};{};{};{};{}".format(model, kms, img, title, link, price, year, maker))

        if len(next_page) > 0:
            browser.follow_link(next_page[0])
            bikes = browser.select('.list-view-item-title a')
            bikes_index = range(0, len(bikes))
        else:
            bikes_index = []
