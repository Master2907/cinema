# Generated by Django 4.0.3 on 2022-03-24 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0006_alter_filmmodel_age_alter_filmmodel_year'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AgeModel',
        ),
        migrations.DeleteModel(
            name='YearModel',
        ),
        migrations.AlterField(
            model_name='filmmodel',
            name='age',
            field=models.CharField(choices=[('1', '6+'), ('2', '8+'), ('3', '12+'), ('4', '16+'), ('4', '18+')], default=3, max_length=3, verbose_name='age'),
        ),
        migrations.AlterField(
            model_name='filmmodel',
            name='movie_type',
            field=models.CharField(choices=[('1', 'film'), ('2', 'cartoon')], default=1, max_length=20, verbose_name='movie type'),
        ),
        migrations.AlterField(
            model_name='filmmodel',
            name='year',
            field=models.IntegerField(choices=[('1', '1900'), ('2', '1901'), ('3', '1902'), ('4', '1903'), ('5', '1904'), ('6', '1905'), ('7', '1906'), ('8', '1907'), ('9', '1908'), ('10', '1909'), ('11', '1910'), ('12', '1911'), ('13', '1912'), ('14', '1913'), ('15', '1914'), ('16', '1915'), ('17', '1916'), ('18', '1917'), ('19', '1918'), ('20', '1919'), ('21', '1920'), ('22', '1921'), ('23', '1922'), ('24', '1923'), ('25', '1924'), ('26', '1925'), ('27', '1926'), ('28', '1927'), ('29', '1928'), ('30', '1929'), ('31', '1930'), ('32', '1931'), ('33', '1932'), ('34', '1933'), ('35', '1934'), ('36', '1935'), ('37', '1936'), ('38', '1937'), ('39', '1938'), ('40', '1939'), ('41', '1940'), ('42', '1941'), ('43', '1942'), ('44', '1943'), ('45', '1944'), ('46', '1945'), ('47', '1946'), ('48', '1947'), ('49', '1948'), ('50', '1949'), ('51', '1950'), ('52', '1951'), ('53', '1952'), ('54', '1953'), ('55', '1954'), ('56', '1955'), ('57', '1956'), ('58', '1957'), ('59', '1958'), ('60', '1959'), ('61', '1960'), ('62', '1961'), ('63', '1962'), ('64', '1963'), ('65', '1964'), ('66', '1965'), ('67', '1966'), ('68', '1967'), ('69', '1968'), ('70', '1969'), ('71', '1970'), ('72', '1971'), ('73', '1972'), ('74', '1973'), ('75', '1974'), ('76', '1975'), ('77', '1976'), ('78', '1977'), ('79', '1978'), ('80', '1979'), ('81', '1980'), ('82', '1981'), ('83', '1982'), ('84', '1983'), ('85', '1984'), ('86', '1985'), ('87', '1986'), ('88', '1987'), ('89', '1988'), ('90', '1989'), ('91', '1990'), ('92', '1991'), ('93', '1992'), ('94', '1993'), ('95', '1994'), ('96', '1995'), ('97', '1996'), ('98', '1997'), ('99', '1998'), ('100', '1999'), ('101', '2000'), ('102', '2001'), ('103', '2002'), ('104', '2003'), ('105', '2004'), ('106', '2005'), ('107', '2006'), ('108', '2007'), ('109', '2008'), ('110', '2009'), ('111', '2010'), ('112', '2011'), ('113', '2012'), ('114', '2013'), ('115', '2014'), ('116', '2015'), ('117', '2016'), ('118', '2017'), ('119', '2018'), ('120', '2019'), ('121', '2020'), ('122', '2021'), ('123', '2022')], default=('123', '2022'), verbose_name='year'),
        ),
    ]
