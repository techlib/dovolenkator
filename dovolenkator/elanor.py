
__all__ = ['Elanor']

from datetime import date

class Elanor(object):
    def __init__(self, manager):
        self.manager = manager

    def get_correction(self, userid, month):
        #only can get correction for this year
        if (int(month)>12 or int(month) < 0 or int(month) >= date.today().month): #if month isn't valid return error. 0th month is reference to current month
            return "Select month between 0 and month before current in integer. 0 means current month."
        rs = self.manager.db.execute("select cetpv.id_tpv, cetpv.pozn_xml from EGJE_OBJ.cetpv where sysdate between to_date(EGJE_OBJ.CETPV.DAT_NAST, 'YYYY-MM-DD') and to_date(EGJE_OBJ.cetpv.dat_ukon, 'YYYY-MM-DD')")
        tpv_s=""
        for i in rs:
            if str(i[1]).replace(" ","").find('ID:'+userid)!=-1:
                tpv_s = str(i[0])
                break
        if tpv_s == "":
            return "User not found. "
        corr_sql = "select korekce_xml,KOD_OBD from EGJE_OBJ.cemzuct where id_tpv = "+tpv_s
        rs = self.manager.db.execute(corr_sql)
        corr = 0
        today = date.today()
        year = today.year
        for i in rs:
            pos = str(i[0]).find('dov_cerp="')
            p_year = str(i[1])
            p_year = p_year[:4]
            p_month = str(i[1])
            p_month = p_month[5:]
            if (int(p_year)==int(year) and (pos != -1 and ((int(p_month) <= int(month)) or int(month) == 0))):#if year and month are 0 return actual correction if not count only correction relevant to date specified
                cerpani = str(i[0])[pos+10:]
                pos = cerpani.find('"')
                cerpani = cerpani[:pos]
                corr += float(cerpani)
        return str(corr)

	
    def get_starting_days(self, userid):
            rs = self.manager.db.execute("select NVL(cetdovol.nar_rd_br,0)+NVL(cetdovol.nar_rd_mr,0),cetpv.id_toso, cetpv.pozn_xml from EGJE_OBJ.cetpv ,EGJE_OBJ.cetdovol where cetpv.id_tpv = cetdovol.id_tpv and sysdate between to_date(EGJE_OBJ.CETPV.DAT_NAST, 'YYYY-MM-DD') and to_date(EGJE_OBJ.cetpv.dat_ukon, 'YYYY-MM-DD') and to_char(sysdate, 'YYYY') = cetdovol.rok")
            for i in rs:
                if str(i[2]).replace(" ","").find('ID:'+userid)!=-1 and i[0]:
                    return str(i[0])
            return "User not found"

# vim:set sw=4 ts=4 et:
# -*- coding: utf-8 -*-
