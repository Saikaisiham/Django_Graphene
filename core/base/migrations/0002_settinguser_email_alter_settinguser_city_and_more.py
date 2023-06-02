# Generated by Django 4.2.1 on 2023-05-31 17:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='settinguser',
            name='email',
            field=models.EmailField(default='', max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='settinguser',
            name='city',
            field=models.CharField(choices=[('Afourar', 'Afourar'), ('Agadir', 'Agadir'), ('Agdz', 'Agdz'), ('Aghbala', 'Aghbala'), ('Agni Izimmer', 'Agni Izimmer'), ('Agourai', 'Agourai'), ('Ahfir', 'Ahfir'), ('Ain El Aouda', 'Ain El Aouda'), ('Ain Taoujdate', 'Ain Taoujdate'), ('Ait Daoud', 'Ait Daoud'), ('Ajdir\u200e', 'Ajdir\u200e'), ('Akchour', 'Akchour'), ('Akka', 'Akka'), ('Aklim', 'Aklim'), ('Aknoul\u200e', 'Aknoul\u200e'), ('Al Aroui', 'Al Aroui'), ('Al Hoceïma\u200e', 'Al Hoceïma\u200e'), ('Alnif', 'Alnif'), ('Amalou Ighriben', 'Amalou Ighriben'), ('Amizmiz', 'Amizmiz'), ('Anzi', 'Anzi'), ('Aoufous', 'Aoufous'), ('Aoulouz', 'Aoulouz'), ('Aourir', 'Aourir'), ('Arazane', 'Arazane'), ('Arbaoua', 'Arbaoua'), ('Arfoud', 'Arfoud'), ('Assa', 'Assa'), ('Assahrij', 'Assahrij'), ('Assilah', 'Assilah'), ('Awsard', 'Awsard'), ('Azemmour', 'Azemmour'), ('Azilal', 'Azilal'), ('Azrou', 'Azrou'), ('Aïn Bni Mathar', 'Aïn Bni Mathar'), ('Aïn Cheggag', 'Aïn Cheggag'), ('Aïn Dorij', 'Aïn Dorij'), ('Aïn Erreggada', 'Aïn Erreggada'), ('Aïn Harrouda', 'Aïn Harrouda'), ('Aïn Jemaa', 'Aïn Jemaa'), ('Aïn Karma', 'Aïn Karma'), ('Aïn Leuh', 'Aïn Leuh'), ('Aït Attab', 'Aït Attab'), ('Aït Baha', 'Aït Baha'), ('Aït Boubidmane', 'Aït Boubidmane'), ('Aït Hichem\u200e', 'Aït Hichem\u200e'), ('Aït Iaâza', 'Aït Iaâza'), ('Aït Ishaq', 'Aït Ishaq'), ('Aït Majden', 'Aït Majden'), ('Aït Melloul', 'Aït Melloul'), ('Aït Ourir', 'Aït Ourir'), ('Aït Yalla', 'Aït Yalla'), ('Bab Berred', 'Bab Berred'), ('Bab Taza', 'Bab Taza'), ('Bejaâd', 'Bejaâd'), ('Ben Ahmed', 'Ben Ahmed'), ('Ben Guerir', 'Ben Guerir'), ('Ben Sergao', 'Ben Sergao'), ('Ben Taïeb', 'Ben Taïeb'), ('Ben Yakhlef', 'Ben Yakhlef'), ('Beni Ayat', 'Beni Ayat'), ('Benslimane', 'Benslimane'), ('Berkane', 'Berkane'), ('Berrechid', 'Berrechid'), ('Bhalil', 'Bhalil'), ('Bin elouidane', 'Bin elouidane'), ('Biougra', 'Biougra'), ('Bir Jdid', 'Bir Jdid'), ('Bni Ansar', 'Bni Ansar'), ('Bni Bouayach\u200e', 'Bni Bouayach\u200e'), ('Bni Chiker', 'Bni Chiker'), ('Bni Drar', 'Bni Drar'), ('Bni Hadifa\u200e', 'Bni Hadifa\u200e'), ('Bni Tadjite', 'Bni Tadjite'), ('Bouanane', 'Bouanane'), ('Bouarfa', 'Bouarfa'), ('Boudnib', 'Boudnib'), ('Boufakrane', 'Boufakrane'), ('Bouguedra', 'Bouguedra'), ('Bouhdila', 'Bouhdila'), ('Bouizakarne', 'Bouizakarne'), ('Boujdour\u200e', 'Boujdour\u200e'), ('Boujniba', 'Boujniba'), ('Boulanouare', 'Boulanouare'), ('Boulemane', 'Boulemane'), ('Boumalne-Dadès', 'Boumalne-Dadès'), ('Boumia', 'Boumia'), ('Bouskoura', 'Bouskoura'), ('Bouznika', 'Bouznika'), ('Bradia', 'Bradia'), ('Brikcha', 'Brikcha'), ('Bzou', 'Bzou'), ('Béni Mellal', 'Béni Mellal'), ('Casablanca', 'Casablanca'), ('Chefchaouen', 'Chefchaouen'), ('Chichaoua', 'Chichaoua'), ('Dar Bni Karrich', 'Dar Bni Karrich'), ('Dar Chaoui', 'Dar Chaoui'), ('Dar El Kebdani', 'Dar El Kebdani'), ('Dar Gueddari', 'Dar Gueddari'), ('Dar Oulad Zidouh', 'Dar Oulad Zidouh'), ('Dcheira El Jihadia', 'Dcheira El Jihadia'), ('Debdou', 'Debdou'), ('Demnate', 'Demnate'), ('Deroua', 'Deroua'), ('Douar Kannine', 'Douar Kannine'), ("Dra'a", "Dra'a"), ('Drargua', 'Drargua'), ('Driouch', 'Driouch'), ('Echemmaia', 'Echemmaia'), ('El Aïoun Sidi Mellouk', 'El Aïoun Sidi Mellouk'), ('El Borouj', 'El Borouj'), ('El Gara', 'El Gara'), ('El Guerdane', 'El Guerdane'), ('El Hajeb', 'El Hajeb'), ('El Hanchane', 'El Hanchane'), ('El Jadida', 'El Jadida'), ('El Kelaâ des Sraghna', 'El Kelaâ des Sraghna'), ('El Ksiba', 'El Ksiba'), ('El Marsa\u200e', 'El Marsa\u200e'), ('El Menzel', 'El Menzel'), ('El Ouatia', 'El Ouatia'), ('Elkbab', 'Elkbab'), ('Er-Rich', 'Er-Rich'), ('Errachidia', 'Errachidia'), ('Es-Semara', 'Es-Semara'), ('Essaouira', 'Essaouira'), ('Fam El Hisn', 'Fam El Hisn'), ('Farkhana', 'Farkhana'), ('Figuig', 'Figuig'), ('Fnideq', 'Fnideq'), ('Foum Jamaa', 'Foum Jamaa'), ('Foum Zguid', 'Foum Zguid'), ('Fquih Ben Salah', 'Fquih Ben Salah'), ('Fraïta', 'Fraïta'), ('Fès', 'Fès'), ('Gardmit', 'Gardmit'), ('Ghafsai\u200e', 'Ghafsai\u200e'), ('Ghmate', 'Ghmate'), ('Goulmima', 'Goulmima'), ('Gourrama', 'Gourrama'), ('Guelmim', 'Guelmim'), ('Guercif\u200e', 'Guercif\u200e'), ('Gueznaia', 'Gueznaia'), ('Guigou', 'Guigou'), ('Guisser', 'Guisser'), ('Had Bouhssoussen', 'Had Bouhssoussen'), ('Had Kourt', 'Had Kourt'), ('Haj Kaddour', 'Haj Kaddour'), ('Harhoura', 'Harhoura'), ('Harte Lyamine', 'Harte Lyamine'), ('Hattane', 'Hattane'), ('Hrara', 'Hrara'), ('Ida Ougnidif', 'Ida Ougnidif'), ('Ifrane', 'Ifrane'), ('Ifri', 'Ifri'), ('Igdamen', 'Igdamen'), ("Ighil n'Oumgoun", "Ighil n'Oumgoun"), ('Ighoud', 'Ighoud'), ('Ighounane', 'Ighounane'), ('Ihddaden', 'Ihddaden'), ('Imassine', 'Imassine'), ('Imintanoute', 'Imintanoute'), ('Imouzzer Kandar', 'Imouzzer Kandar'), ('Imouzzer Marmoucha', 'Imouzzer Marmoucha'), ('Imzouren\u200e', 'Imzouren\u200e'), ('Inahnahen\u200e', 'Inahnahen\u200e'), ('Inezgane', 'Inezgane'), ('Irherm', 'Irherm'), ('Issaguen (Ketama)\u200e', 'Issaguen (Ketama)\u200e'), ('Itzer', 'Itzer'), ('Jamâat Shaim', 'Jamâat Shaim'), ('Jaâdar', 'Jaâdar'), ('Jebha', 'Jebha'), ('Jerada', 'Jerada'), ('Jorf', 'Jorf'), ('Jorf El Melha', 'Jorf El Melha'), ('Jorf Lasfar', 'Jorf Lasfar'), ('Karia', 'Karia'), ('Karia (El Jadida)\u200e', 'Karia (El Jadida)\u200e'), ('Karia Ba Mohamed\u200e', 'Karia Ba Mohamed\u200e'), ('Kariat Arekmane', 'Kariat Arekmane'), ('Kasba Tadla', 'Kasba Tadla'), ('Kassita', 'Kassita'), ('Kattara', 'Kattara'), ('Kehf Nsour', 'Kehf Nsour'), ("Kelaat-M'Gouna", "Kelaat-M'Gouna"), ('Kerouna', 'Kerouna'), ('Kerrouchen', 'Kerrouchen'), ('Khemis Zemamra', 'Khemis Zemamra'), ('Khenichet', 'Khenichet'), ('Khouribga', 'Khouribga'), ('Khémis Sahel', 'Khémis Sahel'), ('Khémisset', 'Khémisset'), ('Khénifra', 'Khénifra'), ('Ksar El Kébir', 'Ksar El Kébir'), ('Kénitra', 'Kénitra'), ('Laaounate', 'Laaounate'), ('Laayoune\u200e', 'Laayoune\u200e'), ('Lakhsas', 'Lakhsas'), ('Lakhsass', 'Lakhsass'), ('Lalla Mimouna', 'Lalla Mimouna'), ('Lalla Takerkoust', 'Lalla Takerkoust'), ('Larache', 'Larache'), ('Laâtamna', 'Laâtamna'), ('Loudaya', 'Loudaya'), ('Loulad', 'Loulad'), ('Lqliâa', 'Lqliâa'), ('Lâattaouia', 'Lâattaouia'), ("M'diq", "M'diq"), ("M'haya", "M'haya"), ("M'rirt", "M'rirt"), ("M'semrir", "M'semrir"), ('Madagh', 'Madagh'), ('Marrakech', 'Marrakech'), ('Martil', 'Martil'), ('Massa (Maroc)', 'Massa (Maroc)'), ('Mechra Bel Ksiri', 'Mechra Bel Ksiri'), ('Megousse', 'Megousse'), ('Mehdia', 'Mehdia'), ('Meknès\u200e', 'Meknès\u200e'), ('Midar', 'Midar'), ('Midelt', 'Midelt'), ('Missour', 'Missour'), ('Mohammadia', 'Mohammadia'), ('Moqrisset', 'Moqrisset'), ('Moulay Abdallah', 'Moulay Abdallah'), ('Moulay Ali Cherif', 'Moulay Ali Cherif'), ('Moulay Bouazza', 'Moulay Bouazza'), ('Moulay Bousselham', 'Moulay Bousselham'), ('Moulay Brahim', 'Moulay Brahim'), ('Moulay Idriss Zerhoun', 'Moulay Idriss Zerhoun'), ('Moulay Yaâcoub', 'Moulay Yaâcoub'), ('Moussaoua', 'Moussaoua'), ('MyAliCherif', 'MyAliCherif'), ('Mzouda', 'Mzouda'), ('Médiouna', 'Médiouna'), ("N'Zalat Bni Amar", "N'Zalat Bni Amar"), ('Nador', 'Nador'), ('Naima', 'Naima'), ('Oualidia', 'Oualidia'), ('Ouaouizeght', 'Ouaouizeght'), ('Ouaoumana', 'Ouaoumana'), ('Ouarzazate', 'Ouarzazate'), ('Ouazzane', 'Ouazzane'), ('Oued Amlil\u200e', 'Oued Amlil\u200e'), ('Oued Heimer', 'Oued Heimer'), ('Oued Ifrane', 'Oued Ifrane'), ('Oued Laou', 'Oued Laou'), ('Oued Rmel', 'Oued Rmel'), ('Oued Zem', 'Oued Zem'), ('Oued-Eddahab', 'Oued-Eddahab'), ('Oujda', 'Oujda'), ('Oulad Abbou', 'Oulad Abbou'), ('Oulad Amrane', 'Oulad Amrane'), ('Oulad Ayad', 'Oulad Ayad'), ('Oulad Berhil', 'Oulad Berhil'), ('Oulad Frej', 'Oulad Frej'), ('Oulad Ghadbane', 'Oulad Ghadbane'), ("Oulad H'Riz Sahel", "Oulad H'Riz Sahel"), ("Oulad M'Barek", "Oulad M'Barek"), ("Oulad M'rah", "Oulad M'rah"), ('Oulad Saïd', 'Oulad Saïd'), ('Oulad Sidi Ben Daoud', 'Oulad Sidi Ben Daoud'), ('Oulad Teïma', 'Oulad Teïma'), ('Oulad Yaich', 'Oulad Yaich'), ('Oulad Zbair\u200e', 'Oulad Zbair\u200e'), ('Ouled Tayeb', 'Ouled Tayeb'), ('Oulmès', 'Oulmès'), ('Ounagha', 'Ounagha'), ('Outat El Haj', 'Outat El Haj'), ('Point Cires', 'Point Cires'), ('Rabat', 'Rabat'), ('Ras El Aïn', 'Ras El Aïn'), ('Ras El Ma', 'Ras El Ma'), ('Ribate El Kheir', 'Ribate El Kheir'), ('Rissani', 'Rissani'), ('Rommani', 'Rommani'), ('Sabaa Aiyoun', 'Sabaa Aiyoun'), ('Safi', 'Safi'), ('Salé', 'Salé'), ('Sarghine', 'Sarghine'), ('Saïdia', 'Saïdia'), ('Sebt El Maârif', 'Sebt El Maârif'), ('Sebt Gzoula', 'Sebt Gzoula'), ('Sebt Jahjouh', 'Sebt Jahjouh'), ('Selouane', 'Selouane'), ('Settat', 'Settat'), ("Sid L'Mokhtar", "Sid L'Mokhtar"), ('Sid Zouin', 'Sid Zouin'), ('Sidi Abdallah Ghiat', 'Sidi Abdallah Ghiat'), ('Sidi Addi', 'Sidi Addi'), ('Sidi Ahmed', 'Sidi Ahmed'), ('Sidi Ali Ban Hamdouche', 'Sidi Ali Ban Hamdouche'), ('Sidi Allal El Bahraoui', 'Sidi Allal El Bahraoui'), ('Sidi Allal Tazi', 'Sidi Allal Tazi'), ('Sidi Bennour', 'Sidi Bennour'), ('Sidi Bou Othmane', 'Sidi Bou Othmane'), ('Sidi Boubker', 'Sidi Boubker'), ('Sidi Bouknadel', 'Sidi Bouknadel'), ('Sidi Bouzid', 'Sidi Bouzid'), ('Sidi Ifni', 'Sidi Ifni'), ('Sidi Jaber', 'Sidi Jaber'), ('Sidi Kacem', 'Sidi Kacem'), ('Sidi Lyamani', 'Sidi Lyamani'), ('Sidi Mohamed ben Abdallah el-Raisuni', 'Sidi Mohamed ben Abdallah el-Raisuni'), ('Sidi Rahhal', 'Sidi Rahhal'), ('Sidi Rahhal Chataï', 'Sidi Rahhal Chataï'), ('Sidi Slimane', 'Sidi Slimane'), ('Sidi Slimane Echcharaa', 'Sidi Slimane Echcharaa'), ('Sidi Smaïl', 'Sidi Smaïl'), ('Sidi Taibi', 'Sidi Taibi'), ('Sidi Yahya El Gharb', 'Sidi Yahya El Gharb'), ('Skhinate', 'Skhinate'), ('Skhirate', 'Skhirate'), ('Skhour Rehamna', 'Skhour Rehamna'), ('Skoura', 'Skoura'), ('Smimou', 'Smimou'), ('Soualem', 'Soualem'), ('Souk El Arbaa', 'Souk El Arbaa'), ('Souk Sebt Oulad Nemma', 'Souk Sebt Oulad Nemma'), ('Stehat', 'Stehat'), ('Séfrou', 'Séfrou'), ('Tabounte', 'Tabounte'), ('Tafajight', 'Tafajight'), ('Tafetachte', 'Tafetachte'), ('Tafraout', 'Tafraout'), ('Taghjijt', 'Taghjijt'), ('Taghzout', 'Taghzout'), ('Tagzen', 'Tagzen'), ('Tahannaout', 'Tahannaout'), ('Tahla\u200e', 'Tahla\u200e'), ('Tala Tazegwaght\u200e', 'Tala Tazegwaght\u200e'), ('Taliouine', 'Taliouine'), ('Talmest', 'Talmest'), ('Talsint', 'Talsint'), ('Tamallalt', 'Tamallalt'), ('Tamanar', 'Tamanar'), ('Tamansourt', 'Tamansourt'), ('Tamassint\u200e', 'Tamassint\u200e'), ('Tamegroute', 'Tamegroute'), ('Tameslouht', 'Tameslouht'), ('Tamesna', 'Tamesna'), ('Tamraght', 'Tamraght'), ('Tan-Tan', 'Tan-Tan'), ('Tanalt', 'Tanalt'), ('Tanger\u200e', 'Tanger\u200e'), ('Tanoumrite Nkob Zagora', 'Tanoumrite Nkob Zagora'), ('Taounate\u200e', 'Taounate\u200e'), ('Taourirt', 'Taourirt'), ('Taourirt ait zaghar', 'Taourirt ait zaghar'), ('Tarfaya\u200e', 'Tarfaya\u200e'), ('Targuist\u200e', 'Targuist\u200e'), ('Taroudannt', 'Taroudannt'), ('Tata', 'Tata'), ('Taza\u200e', 'Taza\u200e'), ('Taïnaste\u200e', 'Taïnaste\u200e'), ('Temsia', 'Temsia'), ('Tendrara', 'Tendrara'), ('Thar Es-Souk\u200e', 'Thar Es-Souk\u200e'), ('Tichoute', 'Tichoute'), ('Tiddas', 'Tiddas'), ('Tiflet', 'Tiflet'), ('Tifnit', 'Tifnit'), ('Tighassaline', 'Tighassaline'), ('Tighza', 'Tighza'), ('Timahdite', 'Timahdite'), ('Tinejdad', 'Tinejdad'), ('Tisgdal', 'Tisgdal'), ('Tissa\u200e', 'Tissa\u200e'), ('Tit Mellil', 'Tit Mellil'), ('Tizguite', 'Tizguite'), ('Tizi Ouasli\u200e', 'Tizi Ouasli\u200e'), ('Tiznit', 'Tiznit'), ('Tiztoutine', 'Tiztoutine'), ('Touarga', 'Touarga'), ('Touima', 'Touima'), ('Touissit', 'Touissit'), ('Toulal', 'Toulal'), ('Toundoute', 'Toundoute'), ('Tounfite', 'Tounfite'), ('Témara', 'Témara'), ('Tétouan\u200e', 'Tétouan\u200e'), ('Youssoufia', 'Youssoufia'), ('Zag', 'Zag'), ('Zagora', 'Zagora'), ("Zaouia d'Ifrane", "Zaouia d'Ifrane"), ('Zaouïat Cheikh', 'Zaouïat Cheikh'), ('Zaïda', 'Zaïda'), ('Zaïo', 'Zaïo'), ('Zeghanghane', 'Zeghanghane'), ('Zeubelemok', 'Zeubelemok'), ('Zinat', 'Zinat')], max_length=100),
        ),
        migrations.AlterField(
            model_name='settinguser',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='setting_user', to='base.userr'),
        ),
    ]