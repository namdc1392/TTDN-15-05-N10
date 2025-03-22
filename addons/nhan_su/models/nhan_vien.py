# from odoo import models, fields, api

# class NhanVien(models.Model):
#     _name = 'nhan_vien'
#     _description = 'Bảng chứa thông tin nhân viên'
#     _rec_name = 'ho_va_ten' 
#     ma_dinh_danh = fields.Char("Mã định danh", required=True)
    
#     ho_va_ten_dem = fields.Char(string="Họ và tên đệm")
#     ten = fields.Char(string="Tên")
#     ho_va_ten = fields.Char(string="Họ và Tên", compute="_compute_ho_va_ten", store=True)

#     ngay_sinh = fields.Date("Ngày sinh")
#     que_quan = fields.Char("Quê quán")
#     email = fields.Char("Email")
#     so_dien_thoai = fields.Char("Số điện thoại")
#     lich_su_cong_tac_ids = fields.One2many("lich_su_cong_tac", inverse_name="nhan_vien_id", string="Lịch sử công tác")
#     don_xin_nghi_ids = fields.One2many('don_xin_nghi', 'nhan_vien_id', string="Đơn xin nghỉ")

#     @api.depends('ho_va_ten_dem', 'ten')
#     def _compute_ho_va_ten(self):  
#         for record in self:
#             record.ho_va_ten = f"{record.ho_va_ten_dem or ''} {record.ten or ''}".strip()


from odoo import models, fields, api

class NhanVien(models.Model):
    _name = 'nhan_vien'
    _description = 'Bảng chứa thông tin nhân viên'
    _rec_name = 'ho_va_ten' 

    ma_dinh_danh = fields.Char("Mã định danh", required=True)
    ho_va_ten_dem = fields.Char(string="Họ và tên đệm")
    ten = fields.Char(string="Tên")
    ho_va_ten = fields.Char(
        string="Họ và Tên", compute="_compute_ho_va_ten", store=True
    )

    ngay_sinh = fields.Date("Ngày sinh")
    que_quan = fields.Char("Quê quán")
    email = fields.Char("Email")
    so_dien_thoai = fields.Char("Số điện thoại")
    
    # don_xin_nghi_ids = fields.One2many('don_xin_nghi', 'nhan_vien_id', string="Đơn xin nghỉ", auto_join=True)
    # lich_theo_doi_nghi_ids = fields.One2many('lich_theo_doi_nghi', 'nhan_vien_id', string="Lịch theo dõi nghỉ")

    lich_su_cong_tac_ids = fields.One2many(
        "lich_su_cong_tac", 'nhan_vien_id', string="Lịch sử công tác"
    )

    @api.depends('ho_va_ten_dem', 'ten')
    def _compute_ho_va_ten(self):  
        for record in self:
            record.ho_va_ten = f"{record.ho_va_ten_dem or ''} {record.ten or ''}".strip()
