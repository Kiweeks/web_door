from urllib.parse import urlparse
from bs4 import BeautifulSoup
from os.path import join
from threading import Thread
import requests
import sqlite3
from PIL import Image
import io

links = (
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_shponirovannye_tekona_freim_03_so_steklom_dub_art-F0000051119',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_shponirovannye_tekona_freim_03_gluhoe_iasen_biskvit_art-F0000050592',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_shponirovannye_tekona_freim_03_so_steklom_iasen_biskvit_art-F0000050597',

    'https://dver.com/mezhkomnatnye-dveri/all/dveri_shponirovannye_tekona_strato_02_so_steklom_tonirovannyi_chernyi_dub_art-F0000050536',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_shponirovannye_tekona_strato_02_so_steklom_iasen_aisberg_art-F0000050541',

    'https://dver.com/mezhkomnatnye-dveri/all/dveri_krashenye__emal__tekona_smalta_01_gluhoe_molochnyi_ral_9010_art-F0000059246',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_krashenye__emal__tekona_smalta_01_gluhoe_belyi_ral_9003_art-F0000052451',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_krashenye__emal__tekona_smalta_01_gluhoe_slonovaia_kost_ral_1013_art-F0000053878',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_krashenye__emal__tekona_smalta_01_so_steklom_slonovaia_kost_ral_1013_art-F0000053883',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_krashenye__emal__tekona_smalta_01_so_steklom_belyi_ral_9003_art-F0000052455',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_krashenye__emal__tekona_smalta_01_so_steklom_molochnyi_ral_9010_art-F0000059252',

    'https://dver.com/mezhkomnatnye-dveri/all/dveri_krashenye__emal__tekona_smalta_02_so_steklom_belyi_ral_9003_art-F0000057650',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_krashenye__emal__tekona_smalta_02_so_steklom_slonovaia_kost_ral_1013_art-F0000053870',
    #
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_krashenye__emal__tekona_smalta_02_gluhoe_belyi_ral_9003_art-F0000057649',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_krashenye__emal__tekona_smalta_02_gluhoe_slonovaia_kost_ral_1013_art-F0000053869',

    'https://dver.com/mezhkomnatnye-dveri/all/dveri_krashenye__emal__tekona_smalta_04_gluhoe_belyi_ral_9003_patina_zoloto_art-F0000054068',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_krashenye__emal__tekona_smalta_04_gluhoe_belyi_ral_9003_patina_serebro_art-F0000052610',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_krashenye__emal__tekona_smalta_04_gluhoe_slonovaia_kost_ral_1013_patina_zoloto_art-F0000054011',
    #
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_krashenye__emal__tekona_smalta_04_so_steklom_belyi_ral_9003_patina_zoloto_art-F0000054072',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_krashenye__emal__tekona_smalta_04_so_steklom_belyi_ral_9003_patina_serebro_art-F0000093378',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_krashenye__emal__tekona_smalta_04_so_steklom_slonovaia_kost_ral_1013_patina_zoloto_art-F0000093373',

    'https://dver.com/mezhkomnatnye-dveri/all/dveri_krashenye__emal__tekona_smalta_05_gluhoe_belyi_ral_9003_patina_zoloto_art-F0000052619',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_krashenye__emal__tekona_smalta_05_gluhoe_slonovaia_kost_ral_1013_art-F0000054017',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_krashenye__emal__tekona_smalta_05_gluhoe_belyi_ral_9003_patina_serebro_art-F0000054076',
    #
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_krashenye__emal__tekona_smalta_05_so_steklom_belyi_ral_9003_patina_zoloto_art-F0000052623',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_krashenye__emal__tekona_smalta_05_so_steklom_slonovaia_kost_ral_1013_art-F0000054023',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_krashenye__emal__tekona_smalta_05_so_steklom_belyi_ral_9003_patina_serebro_art-F0000054080',

    'https://dver.com/mezhkomnatnye-dveri/all/dveri_krashenye__emal__tekona_smalta_06_gluhoe_molochnyi_ral_9010_art-F0000059343',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_krashenye__emal__tekona_smalta_06_gluhoe_slonovaia_kost_ral_1013_art-F0000051244',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_krashenye__emal__tekona_smalta_06_gluhoe_belyi_ral_9003_art-F0000051220',
    #
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_krashenye__emal__tekona_smalta_06_so_steklom_slonovaia_kost_ral_1013_art-F0000051245',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_krashenye__emal__tekona_smalta_06_so_steklom_molochnyi_ral_9010_art-F0000059339',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_krashenye__emal__tekona_smalta_06_so_steklom_belyi_ral_9003_art-F0000051224',

    'https://dver.com/mezhkomnatnye-dveri/all/dveri_krashenye__emal__tekona_smalta_07_gluhoe_slonovaia_kost_ral_1013_art-F0000055165',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_krashenye__emal__tekona_smalta_07_gluhoe_belyi_ral_9003_art-F0000055179',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_krashenye__emal__tekona_smalta_07_gluhoe_molochnyi_ral_9010_art-F0000059348',
    #
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_krashenye__emal__tekona_smalta_07_so_steklom_slonovaia_kost_ral_1013_art-F0000055169',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_krashenye__emal__tekona_smalta_07_so_steklom_belyi_ral_9003_art-F0000055183',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_krashenye__emal__tekona_smalta_07_so_steklom_molochnyi_ral_9010_art-F0000059352',

    'https://dver.com/mezhkomnatnye-dveri/all/dveri_krashenye__emal__tekona_smalta-sharm_11_gluhoe_belyi_ral_9003_art-F0000101175',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_krashenye__emal__tekona_smalta-sharm_11_gluhoe_lvory_art-F0000095822',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_krashenye__emal__tekona_smalta-sharm_11_gluhoe_clear_art-F0000095818',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_krashenye__emal__tekona_smalta-sharm_11_gluhoe_molochnyi_ral_9010_art-F0000098919',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_krashenye__emal__tekona_smalta-sharm_11_gluhoe_malva_art-F0000095826',
    #
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_krashenye__emal__tekona_smalta-sharm_11_so_steklom_belyi_ral_9003_art-F0000101233',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_krashenye__emal__tekona_smalta-sharm_11_so_steklom_lvory_art-F0000095830',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_krashenye__emal__tekona_smalta-sharm_11_so_steklom_clear_art-F0000095836',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_krashenye__emal__tekona_smalta-sharm_11_so_steklom_molochnyi_ral_9010_art-F0000098923',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_krashenye__emal__tekona_smalta-sharm_11_so_steklom_malva_art-F0000095834',

    'https://dver.com/mezhkomnatnye-dveri/all/dveri_krashenye__emal__tekona_smalta-sharm_12_gluhoe_lvory_art-F0000095842',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_krashenye__emal__tekona_smalta-sharm_12_gluhoe_belyi_ral_9003_art-F0000101250',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_krashenye__emal__tekona_smalta-sharm_12_gluhoe_molochnyi_ral_9010_art-F0000095850',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_krashenye__emal__tekona_smalta-sharm_12_gluhoe_malva_art-F0000095858',
    #
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_krashenye__emal__tekona_smalta-sharm_12_so_steklom_lvory_art-F0000095846',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_krashenye__emal__tekona_smalta-sharm_12_so_steklom_belyi_ral_9003_art-F0000102964',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_krashenye__emal__tekona_smalta-sharm_12_so_steklom_belyi_ral_9003_art-F0000102964',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_krashenye__emal__tekona_smalta-sharm_12_so_steklom_malva_art-F0000095862',

    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_ps-03_so_steklom_venge_melinga_art-F0000039833',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_ps-03_so_steklom_grei_melinga_art-F0000044571',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_ps-03_so_steklom_kapuchino_melinga_art-F0000044487',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_ps-03_so_steklom_eshvait_melinga_art-F0000039519',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_ps-03_so_steklom_perlamutrovyi_dub_art-F0000046749',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_ps-03_so_steklom_mokko_art-F0000045758',

    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_ps-07_so_steklom_mokko_art-F0000039364',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_ps-07_so_steklom_oreh_pasadena_art-F0000048299',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_ps-07_so_steklom_venge_melinga_art-F0000039360',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_ps-07_so_steklom_grei_melinga_art-F0000039852',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_ps-07_so_steklom_kapuchino_melinga_art-F0000039856',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_ps-07_so_steklom_perlamutrovyi_dub_art-F0000039357',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_ps-07_so_steklom_eshvait_melinga_art-F0000039633',

    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_ps-07g_gluhoe_venge_melinga_art-F0000046397',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_ps-07g_gluhoe_grei_melinga_art-F0000046331',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_ps-07g_gluhoe_kapuchino_melinga_art-F0000043812',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_ps-07g_gluhoe_mokko_art-F0000046335',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_ps-07g_gluhoe_perlamutrovyi_dub_art-F0000047265',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_ps-07g_gluhoe_eshvait_melinga_art-F0000044693',

    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_ps-35_so_steklom_mokko_art-F0000047737',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_ps-35_so_steklom_venge_melinga_art-F0000045462',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_ps-35_so_steklom_kapuchino_melinga_art-F0000045457',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_ps-35_so_steklom_oreh_pasadena_art-F0000050462',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_ps-35_so_steklom_perlamutrovyi_dub_art-F0000055754',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_ps-35_so_steklom_eshvait_melinga_art-F0000045766',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_ps-35_so_steklom_grei_melinga_art-F0000048620',

    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_ps-40_so_steklom_eshvait_melinga_art-F0000044820',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_ps-40_so_steklom_perlamutrovyi_dub_art-F0000047150',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_ps-40_so_steklom_venge_melinga_art-F0000044825',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_ps-40_so_steklom_grei_melinga_art-F0000045111',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_ps-40_so_steklom_kapuchino_melinga_art-F0000044799',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_ps-40_so_steklom_mokko_art-F0000046322',

    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_psc-10_so_steklom_agat_art-F0000096104',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_psc-10_so_steklom_belyi_art-F0000096128',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_psc-10_so_steklom_grafit_art-F0000096152',

    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_psc-17_so_steklom_belyi_art-F0000050868',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_psc-17_so_steklom_agat_art-F0000081559',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_psc-17_so_steklom_grafit_art-F0000081566',

    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_psc-33_so_steklom_agat_art-F0000081573',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_psc-33_so_steklom_belyi_art-F0000081580',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_psc-33_so_steklom_grafit_art-F0000081585',

    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_psc-25_so_steklom_magnoliia_art-F0000049507',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_psc-25_so_steklom_belyi_art-F0000049522',

    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_psc-26_gluhoe_belyi_art-F0000049566',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_psc-26_gluhoe_magnoliia_art-F0000049514',

    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_psc-28_gluhoe_magnoliia_art-F0000049645',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_psc-28_gluhoe_belyi_art-F0000049434',

    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_psc-30_gluhoe_belyi_art-F0000049438',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_psc-30_gluhoe_magnoliia_art-F0000049726',

    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_psc-35_so_steklom_belyi_art-F0000095641',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_psc-35_so_steklom_agat_art-F0000095637',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_psc-35_so_steklom_zefir_art-F0000096442',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_psc-35_so_steklom_magnoliia_art-F0000095645',

    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_psc-37_so_steklom_belyi_art-F0000095653',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_psc-37_so_steklom_magnoliia_art-F0000095657',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_psc-37_so_steklom_agat_art-F0000095649',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_psc-37_so_steklom_zefir_art-F0000096452',

    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_psc-38_gluhoe_belyi_art-F0000095382',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_psc-38_gluhoe_agat_art-F0000095376',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_psc-38_gluhoe_zefir_art-F0000096458',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_psc-38_gluhoe_magnoliia_art-F0000095388',

    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_psc-41_so_steklom_agat_art-F0000095681',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_psc-41_so_steklom_grafit_art-F0000096220',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_psc-41_so_steklom_belyi_art-F0000095677',

    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_psc-43_so_steklom_agat_art-F0000095697',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_psc-43_so_steklom_grafit_art-F0000096228',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_psc-43_so_steklom_zefir_art-F0000096480',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_psc-43_so_steklom_magnoliia_art-F0000095705',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_psc-43_so_steklom_belyi_art-F0000095701',

    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_psc-56_gluhoe_agat_art-F0000103355',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_psc-56_gluhoe_belyi_art-F0000103361',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_psc-56_gluhoe_grafit_art-F0000103367',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_psc-56_gluhoe_zefir_art-F0000103373',

    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_psc-57_so_steklom_agat_art-F0000103976',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_psc-57_so_steklom_belyi_art-F0000103980',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_psc-57_so_steklom_grafit_art-F0000103984',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_psc-57_so_steklom_zefir_art-F0000103988',

    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_px-1_chernaia_kromka_s_4-h_st__gluhoe_agat_art-F0000099962',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_px-1_chernaia_kromka_s_4-h_st__gluhoe_belyi_art-F0000093464',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_px-1_chernaia_kromka_s_4-h_st__gluhoe_grafit_art-F0000099663',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_px-1_chernaia_kromka_s_4-h_st__gluhoe_dub_arktik_art-F0000089290',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_px-1_chernaia_kromka_s_4-h_st__gluhoe_dub_pacifik_art-F0000088088',

    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_px-7_chernaia_kromka_s_4-h_st__so_steklom_grafit_art-F0000093644',

    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_px-10_chernaia_kromka_s_4-h_st__so_steklom_belyi_art-F0000104164',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_px-10_chernaia_kromka_s_4-h_st__so_steklom_grafit_art-F0000093639',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_px-10_chernaia_kromka_s_4-h_st__so_steklom_dub_arktik_art-F0000088894',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_px-10_chernaia_kromka_s_4-h_st__so_steklom_dub_pacifik_art-F0000088958',

    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_px-16_chernaia_kromka_s_4-h_st__so_steklom_agat_art-F0000094938',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_px-16_chernaia_kromka_s_4-h_st__so_steklom_belyi_art-F0000104573',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_px-16_chernaia_kromka_s_4-h_st__so_steklom_grafit_art-F0000094855',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_px-16_chernaia_kromka_s_4-h_st__so_steklom_dub_skai_belyi_art-F0000094626',

    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_px-18_chernaia_kromka_s_4-h_st__so_steklom_belyi_art-F0000100179',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_px-18_chernaia_kromka_s_4-h_st__so_steklom_dub_arktik_art-F0000089020',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_px-18_chernaia_kromka_s_4-h_st__so_steklom_dub_pacifik_art-F0000089068',

    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_px-19_chernaia_kromka_s_4-h_st__gluhoe_s_moldingom_agat_art-F0000093504',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_px-19_chernaia_kromka_s_4-h_st__gluhoe_s_moldingom_belyi_art-F0000093497',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_px-19_chernaia_kromka_s_4-h_st__gluhoe_s_moldingom_grafit_art-F0000094001',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_px-19_chernaia_kromka_s_4-h_st__gluhoe_s_moldingom_magnoliia_art-F0000093508',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_px-19_chernaia_kromka_s_4-h_st__gluhoe_s_moldingom_seryi_beton_art-F0000094049',

    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_px-2_al_kromka_s_4-h_st__gluhoe_s_moldingom_agat_art-F0000094915',

    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_px-8_al_kromka_s_4-h_st__so_steklom_agat_art-F0000095176',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_px-8_al_kromka_s_4-h_st__so_steklom_belyi_art-F0000088772',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_px-8_al_kromka_s_4-h_st__so_steklom_grafit_art-F0000102736',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_px-8_al_kromka_s_4-h_st__so_steklom_dub_arktik_art-F0000089119',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_px-8_al_kromka_s_4-h_st__so_steklom_dub_pacifik_art-F0000089179',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_px-8_al_kromka_s_4-h_st__so_steklom_dub_skai_belyi_art-F0000102547',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_px-8_al_kromka_s_4-h_st__so_steklom_seryi_beton_art-F0000093366',

    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_px-10_al_kromka_s_2-h_st__so_steklom_belyi_art-F0000076657',

    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_px-11_al_kromka_s_4-h_st__so_steklom_agat_art-F0000092066',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_px-11_al_kromka_s_4-h_st__so_steklom_belyi_art-F0000092528',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_px-11_al_kromka_s_4-h_st__so_steklom_dub_skai_belyi_art-F0000088842',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_px-11_al_kromka_s_4-h_st__so_steklom_seryi_beton_art-F0000092443',

    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_px-15_al_kromka_s_4-h_st__gluhoe_s_moldingom_seryi_beton_art-F0000096356',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_px-15_al_kromka_s_4-h_st__gluhoe_s_moldingom_dub_skai_belyi_art-F0000090679',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_px-15_al_kromka_s_4-h_st__gluhoe_s_moldingom_grafit_art-F0000093207',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_px-15_al_kromka_s_4-h_st__gluhoe_s_moldingom_agat_art-F0000091161',

    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_px-18_al_kromka_s_2-h_st__so_steklom_agat_art-F0000077248',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_px-18_al_kromka_s_2-h_st__so_steklom_belyi_art-F0000077263',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_px-18_al_kromka_s_2-h_st__so_steklom_dub_skai_seryi_art-F0000077330',

    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_pst-10_so_steklom_belyi_barhat_art-F0000090106',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_pst-10_so_steklom_belyi_iasen_art-F0000090124',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_pst-10_so_steklom_seryi_barhat_art-F0000090143',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_pst-10_so_steklom_seryi_iasen_art-F0000090161',

    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_p-20_chernyi_molding_gluhoe_s_moldingom_agat_art-F0000097860',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_p-20_chernyi_molding_gluhoe_s_moldingom_belyi_art-F0000097872',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_p-20_chernyi_molding_gluhoe_s_moldingom_grafit_art-F0000097884',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_ekoshpon__pvh_profilo_porte_p-20_chernyi_molding_gluhoe_s_moldingom_magnoliia_art-F0000097896',

    'https://dver.com/mezhkomnatnye-dveri/all/dveri_iz_massiva_dvernaia_birzha_ampir_dg_gluhoe_tonirovannaia_sosna_art-00123',

    'https://dver.com/mezhkomnatnye-dveri/all/dveri_iz_massiva_dvernaia_birzha_ampir_do_so_steklom_tonirovannaia_sosna_art-F0000066793',
)


def write_result(files: list):
    for file in files:
        with open(join(f'photo_door', file['name']), 'wb') as img:
            img.write(file['data'])


def get_domain(link: str) -> str:
    return urlparse(link).netloc


def as_doors(index: int, link: str) -> dict:
    resp = requests.get(link)
    print(index, link)
    bs = BeautifulSoup(resp.text, 'lxml')

    img = bs.find('img', id='main_image_big')['src']
    full_path = 'https://' + get_domain(link) + f'/{img}'
    name = img.split('/')[-1]

    img_color = tuple(filter(lambda obj: obj['src'].startswith('/xml/colors_images'), bs.find_all('img')))[0]

    COLOR = {
        'code': get_img_color(requests.get(f'https://dver.com/{img_color["src"]}').content),
        'color': img_color['title']
    }

    TITLE = ' '.join(bs.find('h1').text.replace(COLOR['color'], '').split()[:-5])
    BRAND = 'ТЕКОНА'

    CATEGORY_ID = 4
    DOOR_TYPE = 7 if 'стекло' not in TITLE else 8

    SIZES = get_sizes(bs)
    PARAMS = get_params(bs)
    DESCRIPTION = "Наши межкомнатные двери — идеальное сочетание стиля и функциональности. Улучшите интерьер вашего дома, выбрав из нашего разнообразного ассортимента. Инновационные материалы и заботливо продуманный дизайн обеспечивают не только визуальное восхищение, но и долговечность использования. Откройте для себя комфорт и элегантность с нашими межкомнатными дверями, которые подчеркнут уникальность каждого помещения."
    insert_in_db(TITLE, BRAND, CATEGORY_ID, DOOR_TYPE, PARAMS, DESCRIPTION, COLOR, SIZES,
                 {'name': name, 'data': requests.get(full_path).content})


def get_sizes(bs):
    sizes = bs.find('td', id='size_selecting').find_all('div')
    new_sizes = []

    for size in sizes:
        if len(size.text) < 5:
            continue
        a, b = map(lambda x: x.strip() + '0', size.text.split(' х '))
        new_sizes.append(f'{a} х {b} мм')

    return {*new_sizes}


def get_params(bs):
    params = bs.find('table', id='opisanie_table').find_all('tr')[1:-1]
    params_str = ''
    for param in params:
        key = param.find('strong')
        if key is None:
            continue
        key = key.text.strip()
        value = param.find_all('td')[-1].text.strip()
        params_str += f'{key}: {value}\n'
    return params_str


def insert_in_db(title, brand, category_id, type_id, params, description, color, sizes, img):
    write_result(files=[img])
    db_path = r'C:\Users\Hiro\Documents\GitHub\web_door\kiweeks\db.sqlite3'
    con = sqlite3.connect(db_path)
    cur = con.cursor()

    id = cur.execute('INSERT INTO main_door (title, brand, properties, type_id, category_id, description)'
                     'VALUES (?,?,?,?,?,?);', (title, brand, params, type_id, category_id, description)).lastrowid

    cur.execute('INSERT INTO main_photo_door (doors_id, photos) VALUES (?, ?)', (id, 'photo_door/'+img['name']))
    color_id = cur.execute("SELECT id FROM main_color_inside WHERE code = ?", (color['code'],)).fetchone()
    print(color_id)
    if color_id is None:
        color_id = cur.execute("INSERT INTO main_color_inside (color, code) VALUES (?, ?)", (color['color'],color['code'])).lastrowid
    else:
        color_id = color_id[0]

    cur.execute("INSERT INTO main_door_colors_inside (door_id, color_inside_id) VALUES (?, ?)",(id, color_id))
    cur.execute("INSERT INTO main_door_sides (door_id, side_of_door_id) VALUES (?, 1), (?, 2)",(id, id))
    for size in sizes:
        size_id = cur.execute("SELECT id FROM main_size_door WHERE sizes_doors = ?", (size,)).fetchone()
        if size_id is None:
            size_id = cur.execute("INSERT INTO main_size_door (sizes_doors ) VALUES (?)", (size, )).lastrowid
        else:
            size_id = size_id[0]

        cur.execute("INSERT INTO main_door_sizes (door_id, size_door_id) VALUES (?,?)", (id, size_id))
    con.commit()
    cur.close()


def get_img_color(img_bytes):
    im = Image.open(io.BytesIO(img_bytes))  # Can be many different formats.
    rgb_im = im.convert('RGB')
    r, g, b = rgb_im.getpixel((1, 1))
    return '{:02x}{:02x}{:02x}'.format(r, g, b)


if __name__ == '__main__':
    a = 0
    q = []
    for index, link in enumerate(links, start=1):
        as_doors(index, link)
