# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

from django.db import models

class AccessLog(models.Model):
    idaccesslog = models.AutoField(db_column='idAccessLog', primary_key=True)  # Field name made lowercase.
    iduser = models.ForeignKey('Users', models.DO_NOTHING, db_column='idUser')  # Field name made lowercase.
    system = models.CharField(max_length=18)
    ip = models.CharField(max_length=18)
    useragent = models.CharField(db_column='userAgent', max_length=150)  # Field name made lowercase.
    date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'access_log'


class ActualDates(models.Model):
    id = models.AutoField(db_column='id', primary_key=True) 
    idorder = models.ForeignKey('Orders', models.DO_NOTHING, db_column='idOrder')  # Field name made lowercase.
    days_to_deliver = models.IntegerField()
    date_delivery_promise = models.DateTimeField(blank=True, null=True)
    actual_pickup = models.DateTimeField(blank=True, null=True)
    actual_delivery = models.DateTimeField(blank=True, null=True)
    received_by = models.CharField(max_length=191, blank=True, null=True)
    date_delivery_promise_2 = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'actual_dates'


class Addresses(models.Model):
    idaddress = models.AutoField(db_column='idAddress', primary_key=True)  # Field name made lowercase.
    label = models.CharField(max_length=250, blank=True, null=True)
    firstname = models.CharField(db_column='firstName', max_length=150, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='lastName', max_length=150, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(max_length=250, blank=True, null=True)
    company = models.CharField(max_length=100, blank=True, null=True)
    rfc = models.CharField(db_column='RFC', max_length=13, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(max_length=45, blank=True, null=True)
    address1 = models.CharField(max_length=250, blank=True, null=True)
    externalnumber = models.CharField(db_column='externalNumber', max_length=191)  # Field name made lowercase.
    colonia = models.CharField(max_length=250, blank=True, null=True)
    crossstreet = models.CharField(db_column='crossStreet', max_length=35, blank=True, null=True)  # Field name made lowercase.
    reference = models.CharField(max_length=200, blank=True, null=True)
    delegation = models.CharField(max_length=120, blank=True, null=True)
    city = models.CharField(max_length=120, blank=True, null=True)
    zipcode = models.CharField(db_column='zipCode', max_length=18, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(max_length=60, blank=True, null=True)
    country = models.CharField(max_length=60, blank=True, null=True)
    iduser = models.ForeignKey('Users', models.DO_NOTHING, db_column='idUser')  # Field name made lowercase.
    idzipcode = models.IntegerField(db_column='idZipCode', blank=True, null=True)  # Field name made lowercase.
    active = models.IntegerField()
    type = models.CharField(max_length=18)
    senderdefault = models.IntegerField(db_column='senderDefault')  # Field name made lowercase.
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'addresses'


class ApiLog(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    iduser = models.ForeignKey('Users', models.DO_NOTHING, db_column='idUser') # Field name made lowercase.
    request = models.TextField()
    response = models.TextField()
    services = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'api_log'


class Banners(models.Model):
    idbanner = models.AutoField(db_column='idBanner', primary_key=True)  # Field name made lowercase.
    bannerfilename = models.CharField(db_column='bannerFilename', max_length=250)  # Field name made lowercase.
    width = models.IntegerField()
    height = models.IntegerField()
    bannerlink = models.CharField(db_column='bannerLink', max_length=255)  # Field name made lowercase.
    idsection = models.IntegerField(db_column='idSection')  # Field name made lowercase.
    idsectionbanner = models.IntegerField(db_column='idSectionBanner')  # Field name made lowercase.
    bannertext = models.CharField(db_column='bannerText', max_length=250)  # Field name made lowercase.
    description = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'banners'


class BulkQuotations(models.Model):
    idbulkquotation = models.AutoField(db_column='idBulkQuotation', primary_key=True)  # Field name made lowercase.
    iduser = models.IntegerField(db_column='idUser')  # Field name made lowercase.
    groupquotation = models.CharField(db_column='groupQuotation', max_length=25)  # Field name made lowercase.
    orders = models.TextField()
    criteria = models.CharField(max_length=24)
    status = models.IntegerField()
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bulk_quotations'


class CarrierLabel(models.Model):
    idcarrierlabel = models.AutoField(db_column='idCarrierLabel', primary_key=True)  # Field name made lowercase.
    idcarrier = models.IntegerField(db_column='idCarrier')  # Field name made lowercase.
    size = models.CharField(max_length=191)
    type = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'carrier_label'


class Carriers(models.Model):
    idcarrier = models.AutoField(db_column='idCarrier', primary_key=True)  # Field name made lowercase.
    code = models.CharField(max_length=10)
    carrier = models.CharField(max_length=150)
    comercialname = models.CharField(db_column='comercialName', max_length=191, blank=True, null=True)  # Field name made lowercase.
    deadlineminutesmargin = models.IntegerField(db_column='deadlineMinutesMargin')  # Field name made lowercase.
    description = models.TextField(blank=True, null=True)
    imagesmall = models.CharField(db_column='imageSmall', max_length=250, blank=True, null=True)  # Field name made lowercase.
    imagelarge = models.CharField(db_column='imageLarge', max_length=250, blank=True, null=True)  # Field name made lowercase.
    processtype = models.CharField(db_column='processType', max_length=45)  # Field name made lowercase.
    status = models.IntegerField()
    ispro = models.IntegerField(db_column='isPro')  # Field name made lowercase.
    isapi = models.IntegerField(db_column='isApi')  # Field name made lowercase.
    contractdiscount = models.FloatField(db_column='contractDiscount')  # Field name made lowercase.
    hourlimitrecolection = models.CharField(db_column='hourLimitRecolection', max_length=191)  # Field name made lowercase.
    ratetype = models.IntegerField(db_column='rateType')  # Field name made lowercase.
    multipackage = models.IntegerField()
    environment = models.CharField(max_length=18, blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'carriers'


class CashbackAssignmentsToGroups(models.Model):
    id = models.AutoField(db_column='id', primary_key=True) 
    idcashback = models.IntegerField(db_column='idCashback')  # Field name made lowercase.
    idusergroup = models.IntegerField(db_column='idUserGroup')  # Field name made lowercase.
    movement = models.IntegerField()
    created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cashback_assignments_to_groups'


class Cashbacks(models.Model):
    idcashback = models.AutoField(db_column='idCashback', primary_key=True)  # Field name made lowercase.
    cashback = models.CharField(max_length=48)
    from_field = models.IntegerField(db_column='from', blank=True, null=True)  # Field renamed because it was a Python reserved word.
    percentage = models.IntegerField()
    description = models.CharField(max_length=124, blank=True, null=True)
    created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cashbacks'


class ConfigCarriersByUser(models.Model):
    idconfigcarrierbyuser = models.AutoField(db_column='idConfigCarrierByUser', primary_key=True)  # Field name made lowercase.
    iduser = models.IntegerField(db_column='idUser')  # Field name made lowercase.
    idcarrier = models.IntegerField(db_column='idCarrier')  # Field name made lowercase.
    active = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'config_carriers_by_user'


class Configs(models.Model):
    idconfig = models.AutoField(db_column='idConfig', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=45, blank=True, null=True)
    status = models.CharField(max_length=45, blank=True, null=True)
    type = models.CharField(max_length=45, blank=True, null=True)
    values = models.CharField(max_length=120)
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'configs'


class Constraints(models.Model):
    idconstraint = models.AutoField(db_column='idConstraint', primary_key=True)  # Field name made lowercase.
    idzipcode = models.IntegerField(db_column='idZipCode')  # Field name made lowercase.
    idcarrier = models.IntegerField(db_column='idCarrier')  # Field name made lowercase.
    isremote = models.IntegerField(db_column='isRemote')  # Field name made lowercase.
    frequency = models.CharField(max_length=120)
    deniedservices = models.CharField(db_column='deniedServices', max_length=40)  # Field name made lowercase.
    ocurre = models.IntegerField()
    additionaldays = models.CharField(db_column='additionalDays', max_length=40)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'constraints'


class Counters(models.Model):
    id = models.AutoField(db_column='id', primary_key=True) 
    name = models.CharField(max_length=45)
    value = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'counters'


class Countries(models.Model):
    idcountry = models.AutoField(db_column='idCountry', primary_key=True)  # Field name made lowercase.
    country = models.CharField(max_length=250)
    isocode = models.CharField(db_column='isoCode', max_length=2)  # Field name made lowercase.
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'countries'


class Coupons(models.Model):
    idcoupon = models.AutoField(db_column='idCoupon', primary_key=True)  # Field name made lowercase.
    coupon = models.CharField(max_length=150)
    code = models.CharField(max_length=100)
    percentage = models.IntegerField(blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    type = models.IntegerField()
    maxclientuses = models.IntegerField(db_column='maxClientUses')  # Field name made lowercase.
    maxcoupons = models.IntegerField(db_column='maxCoupons')  # Field name made lowercase.
    available = models.IntegerField()
    deleted = models.IntegerField()
    validfrom = models.DateTimeField(db_column='validFrom', blank=True, null=True)  # Field name made lowercase.
    validto = models.DateTimeField(db_column='validTo', blank=True, null=True)  # Field name made lowercase.
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'coupons'


# class Cpload(models.Model):
#     d_codigo = models.CharField(max_length=512, blank=True, null=True)
#     d_asenta = models.CharField(max_length=512, blank=True, null=True)
#     d_tipo_asenta = models.CharField(max_length=512, blank=True, null=True)
#     d_mnpio = models.CharField(db_column='D_mnpio', max_length=512, blank=True, null=True)  # Field name made lowercase.
#     d_estado = models.CharField(max_length=512, blank=True, null=True)
#     d_ciudad = models.CharField(max_length=512, blank=True, null=True)
#     d_cp = models.CharField(db_column='d_CP', max_length=512, blank=True, null=True)  # Field name made lowercase.
#     c_estado = models.CharField(max_length=512, blank=True, null=True)
#     c_oficina = models.CharField(max_length=512, blank=True, null=True)
#     c_cp = models.CharField(db_column='c_CP', max_length=512, blank=True, null=True)  # Field name made lowercase.
#     c_tipo_asenta = models.CharField(max_length=512, blank=True, null=True)
#     c_mnpio = models.CharField(max_length=512, blank=True, null=True)
#     id_asenta_cpcons = models.CharField(max_length=512, blank=True, null=True)
#     d_zona = models.CharField(max_length=512, blank=True, null=True)
#     c_cve_ciudad = models.CharField(max_length=512, blank=True, null=True)
#     idstate = models.IntegerField(db_column='idState', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'cpload'


class CreditBonus(models.Model):
    idcreditbonus = models.AutoField(db_column='idCreditBonus', primary_key=True)  # Field name made lowercase.
    description = models.CharField(max_length=100, blank=True, null=True)
    amount = models.FloatField()
    bonusamount = models.FloatField(db_column='bonusAmount')  # Field name made lowercase.
    bonuspercentage = models.FloatField(db_column='bonusPercentage')  # Field name made lowercase.
    created = models.DateTimeField()
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'credit_bonus'


# class CreditCards(models.Model):
#     id_client = models.IntegerField()
#     id_card = models.CharField(max_length=191)
#     created = models.DateTimeField(blank=True, null=True)
#     modified = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'credit_cards'


# class CreditIncomeLog(models.Model):
#     iduserbackend = models.IntegerField(db_column='idUserBackend')  # Field name made lowercase.
#     iduser = models.IntegerField(db_column='idUser')  # Field name made lowercase.
#     amount = models.FloatField()
#     type = models.IntegerField()
#     timestamp = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'credit_income_log'


class Dealers(models.Model):
    iddealer = models.AutoField(db_column='idDealer', primary_key=True)  # Field name made lowercase.
    idcoupon = models.IntegerField(db_column='idCoupon')  # Field name made lowercase.
    name = models.CharField(max_length=45)
    description = models.CharField(max_length=45, blank=True, null=True)
    commissionpercentage = models.FloatField(db_column='commissionPercentage')  # Field name made lowercase.
    stringid = models.CharField(db_column='stringId', max_length=12)  # Field name made lowercase.
    active = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'dealers'


class DiscountByCarrier(models.Model):
    iddiscountbycarrier = models.AutoField(db_column='idDiscountByCarrier', primary_key=True)  # Field name made lowercase.
    iddiscount = models.ForeignKey('Discounts', models.DO_NOTHING, db_column='idDiscount')  # Field name made lowercase.
    idcarrier = models.ForeignKey(Carriers, models.DO_NOTHING, db_column='idCarrier')  # Field name made lowercase.
    discount = models.FloatField()

    class Meta:
        managed = False
        db_table = 'discount_by_carrier'


class Discounts(models.Model):
    iddiscount = models.AutoField(db_column='idDiscount', primary_key=True)  # Field name made lowercase.
    from_field = models.IntegerField(db_column='from')  # Field renamed because it was a Python reserved word.
    to = models.IntegerField()
    created_at = models.DateTimeField()
    modified_at = models.DateTimeField()
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'discounts'


# class DiscountsChangesLog(models.Model):
#     action = models.CharField(max_length=24)
#     iddiscount = models.ForeignKey(Discounts, models.DO_NOTHING, db_column='idDiscount')  # Field name made lowercase.
#     idcarrier = models.ForeignKey(Carriers, models.DO_NOTHING, db_column='idCarrier', blank=True, null=True)  # Field name made lowercase.
#     from_field = models.FloatField(db_column='from')  # Field renamed because it was a Python reserved word.
#     to = models.FloatField()
#     olddiscount = models.FloatField(db_column='oldDiscount', blank=True, null=True)  # Field name made lowercase.
#     discount = models.FloatField(blank=True, null=True)
#     date = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'discounts_changes_log'


class Ecommerce(models.Model):
    idecommerce = models.AutoField(db_column='idEcommerce', primary_key=True)  # Field name made lowercase.
    ecommerce = models.CharField(max_length=120)
    description = models.CharField(max_length=120)
    status = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ecommerce'


# class EcommerceOrderStatusLog(models.Model):
#     iduserecommerce = models.IntegerField(db_column='idUserEcommerce')  # Field name made lowercase.
#     idecommerceorder = models.CharField(db_column='idEcommerceOrder', max_length=40)  # Field name made lowercase.
#     newstatus = models.CharField(db_column='newStatus', max_length=40, blank=True, null=True)  # Field name made lowercase.
#     request = models.TextField(blank=True, null=True)
#     response = models.TextField(blank=True, null=True)
#     successful = models.IntegerField()
#     message = models.CharField(max_length=180)
#     created_at = models.DateTimeField(blank=True, null=True)
#     updated_at = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'ecommerce_order_status_log'


# class EcommerceProducts(models.Model):
#     iduserecommerce = models.IntegerField(db_column='idUserEcommerce')  # Field name made lowercase.
#     idecommerceproduct = models.CharField(db_column='idEcommerceProduct', max_length=40)  # Field name made lowercase.
#     product = models.CharField(max_length=28)
#     weight = models.FloatField()
#     length = models.FloatField()
#     width = models.FloatField()
#     height = models.FloatField()
#     created_at = models.DateTimeField(blank=True, null=True)
#     updated_at = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'ecommerce_products'


class EcommerceVersions(models.Model):
    idecommerceversion = models.AutoField(db_column='idEcommerceVersion', primary_key=True)  # Field name made lowercase.
    idecommerce = models.IntegerField(db_column='idEcommerce')  # Field name made lowercase.
    version = models.CharField(max_length=120)
    technology = models.CharField(max_length=28, blank=True, null=True)
    status = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ecommerce_versions'


class EventoInnohub(models.Model):
    idrecord = models.AutoField(db_column='idRecord', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    asistencia = models.CharField(max_length=10)
    acompanantes = models.CharField(max_length=255)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'evento_innohub'


class FailedJobs(models.Model):
    id = models.BigAutoField(primary_key=True)
    connection = models.TextField()
    queue = models.TextField()
    payload = models.TextField()
    exception = models.TextField()
    failed_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'failed_jobs'


class GuideErrors(models.Model):
    idguideerror = models.AutoField(db_column='idGuideError', primary_key=True)  # Field name made lowercase.
    idorder = models.ForeignKey('Orders', models.DO_NOTHING, db_column='idOrder')  # Field name made lowercase.
    idusercredit = models.IntegerField(db_column='idUserCredit', blank=True, null=True)  # Field name made lowercase.
    error = models.CharField(max_length=255)
    status = models.SmallIntegerField()
    feedback = models.CharField(max_length=255, blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    trace = models.TextField()

    class Meta:
        managed = False
        db_table = 'guide_errors'


class Guides(models.Model):
    idguide = models.AutoField(db_column='idGuide', primary_key=True)  # Field name made lowercase.
    guide = models.CharField(max_length=45)
    status = models.IntegerField()
    type = models.CharField(max_length=45)
    typeid = models.IntegerField(db_column='typeId')  # Field name made lowercase.
    isadvances = models.IntegerField(db_column='isAdvances')  # Field name made lowercase.
    iduser = models.IntegerField(db_column='idUser', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'guides'


class Insurances(models.Model):
    idinsurance = models.AutoField(db_column='idInsurance', primary_key=True)  # Field name made lowercase.
    idorder = models.ForeignKey('Orders', models.DO_NOTHING, db_column='idOrder')  # Field name made lowercase.
    trackingcode = models.CharField(db_column='trackingCode', max_length=191)  # Field name made lowercase.
    insurancecode = models.CharField(db_column='insuranceCode', max_length=191, blank=True, null=True)  # Field name made lowercase.
    idcarrier = models.IntegerField(db_column='idCarrier')  # Field name made lowercase.
    reference = models.CharField(max_length=191, blank=True, null=True)
    amountinsurancews = models.CharField(db_column='amountInsuranceWS', max_length=191, blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'insurances'


# class IntendPro(models.Model):
#     nombre = models.CharField(max_length=120)
#     posicion = models.CharField(max_length=45)
#     telefono = models.CharField(max_length=24)
#     email = models.CharField(max_length=38)
#     website = models.CharField(max_length=120)
#     created_at = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'intend_pro'


class Jobs(models.Model):
    id = models.BigAutoField(primary_key=True)
    queue = models.CharField(max_length=191)
    payload = models.TextField()
    attempts = models.PositiveIntegerField()
    reserved_at = models.PositiveIntegerField(blank=True, null=True)
    available_at = models.PositiveIntegerField()
    created_at = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'jobs'


class Locations(models.Model):
    idlocation = models.AutoField(db_column='idLocation', primary_key=True)  # Field name made lowercase.
    iduserecommerce = models.IntegerField(db_column='idUserEcommerce')  # Field name made lowercase.
    idlocationitem = models.BigIntegerField(db_column='idLocationItem')  # Field name made lowercase.
    idlocationecommerce = models.BigIntegerField(db_column='idLocationEcommerce')  # Field name made lowercase.
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'locations'


class MatrixZones(models.Model):
    idmatrixzone = models.AutoField(db_column='idMatrixZone', primary_key=True)  # Field name made lowercase.
    idzone = models.ForeignKey('Zones', models.DO_NOTHING, db_column='idZone')  # Field name made lowercase.
    idzipgroupfrom = models.ForeignKey('ZipGroups', models.DO_NOTHING, db_column='idZipGroupFrom', related_name='gameclaim_idZipGroupFrom')  # Field name made lowercase.
    idzipgroupto = models.ForeignKey('ZipGroups', models.DO_NOTHING, db_column='idZipGroupTo', related_name='gameclaim_idZipGroupTo')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'matrix_zones'


# class Migrations(models.Model):
#     migration = models.CharField(max_length=191)
#     batch = models.IntegerField()

#     class Meta:
#         managed = False
#         db_table = 'migrations'


class MultiPayments(models.Model):
    idmultipayment = models.AutoField(db_column='idMultiPayment', primary_key=True)  # Field name made lowercase.
    tax = models.FloatField()
    total = models.FloatField()
    status = models.IntegerField()
    paymentmethod = models.CharField(db_column='paymentMethod', max_length=50)  # Field name made lowercase.
    paymentreference = models.CharField(db_column='paymentReference', max_length=45)  # Field name made lowercase.
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'multi_payments'


class Notifications(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    type = models.CharField(max_length=191)
    notifiable_id = models.PositiveIntegerField()
    notifiable_type = models.CharField(max_length=191)
    data = models.TextField()
    read_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notifications'


class OauthAccessTokens(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    user_id = models.IntegerField(blank=True, null=True)
    client_id = models.IntegerField()
    name = models.CharField(max_length=191, blank=True, null=True)
    scopes = models.TextField(blank=True, null=True)
    revoked = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    expires_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oauth_access_tokens'


class OauthAuthCodes(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    user_id = models.IntegerField()
    client_id = models.IntegerField()
    scopes = models.TextField(blank=True, null=True)
    revoked = models.IntegerField()
    expires_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oauth_auth_codes'


class OauthClients(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=191)
    secret = models.CharField(max_length=100)
    redirect = models.TextField()
    personal_access_client = models.IntegerField()
    password_client = models.IntegerField()
    revoked = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oauth_clients'


class OauthPersonalAccessClients(models.Model):
    client_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oauth_personal_access_clients'


class OauthRefreshTokens(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    access_token_id = models.CharField(max_length=100)
    revoked = models.IntegerField()
    expires_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oauth_refresh_tokens'


# class OffDays(models.Model):
#     idcarrier = models.IntegerField(db_column='idCarrier')  # Field name made lowercase.
#     date = models.DateField()

#     class Meta:
#         managed = False
#         db_table = 'off_days'


class OrderDetails(models.Model):
    idorderdetails = models.AutoField(db_column='idorderDetails', primary_key=True)  # Field name made lowercase.
    idorder = models.ForeignKey('Orders', models.DO_NOTHING, db_column='idOrder')  # Field name made lowercase.
    weight = models.FloatField(blank=True, null=True)
    length = models.FloatField(blank=True, null=True)
    width = models.FloatField(blank=True, null=True)
    height = models.FloatField(blank=True, null=True)
    numberpackage = models.IntegerField(db_column='numberPackage')  # Field name made lowercase.
    numberofpackages = models.IntegerField(db_column='numberOfPackages')  # Field name made lowercase.
    price = models.DecimalField(max_digits=10, decimal_places=2)
    fee = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    trackingcode = models.CharField(db_column='trackingCode', max_length=40, blank=True, null=True)  # Field name made lowercase.
    guia = models.CharField(max_length=60, blank=True, null=True)
    incidence = models.CharField(max_length=191, blank=True, null=True)
    incidencetype = models.CharField(db_column='incidenceType', max_length=191, blank=True, null=True)  # Field name made lowercase.
    statusec = models.CharField(db_column='statusEc', max_length=191, blank=True, null=True)  # Field name made lowercase.
    statusclient = models.CharField(db_column='statusClient', max_length=191, blank=True, null=True)  # Field name made lowercase.
    statusstep = models.CharField(db_column='statusStep', max_length=191, blank=True, null=True)  # Field name made lowercase.
    created = models.DateTimeField()
    modified = models.DateTimeField()
    shippingid = models.CharField(db_column='shippingId', max_length=191)  # Field name made lowercase.
    receiverid = models.CharField(db_column='receiverId', max_length=191)  # Field name made lowercase.
    buyerid = models.CharField(db_column='buyerId', max_length=191)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'order_details'


class OrderStatus(models.Model):
    idorderstatus = models.AutoField(db_column='idOrderStatus', primary_key=True)  # Field name made lowercase.
    orderstatus = models.CharField(db_column='orderStatus', max_length=150)  # Field name made lowercase.
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'order_status'


class OrderStatusLog(models.Model):
    idorderstatuslog = models.AutoField(db_column='idOrderStatusLog', primary_key=True)  # Field name made lowercase.
    idorder = models.IntegerField(db_column='idOrder')  # Field name made lowercase.
    idorderdetails = models.IntegerField(db_column='idorderDetails', blank=True, null=True)  # Field name made lowercase.
    statusec = models.CharField(db_column='statusEc', max_length=120)  # Field name made lowercase.
    statusclient = models.CharField(db_column='statusClient', max_length=120)  # Field name made lowercase.
    incidence = models.IntegerField()
    incidencetype = models.CharField(db_column='incidenceType', max_length=40, blank=True, null=True)  # Field name made lowercase.
    status1 = models.CharField(max_length=45)
    status2 = models.CharField(max_length=45, blank=True, null=True)
    request = models.TextField(blank=True, null=True)
    response = models.TextField(blank=True, null=True)
    logdate = models.DateTimeField(db_column='logDate')  # Field name made lowercase.
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_status_log'


class Orders(models.Model):
    idorder = models.AutoField(db_column='idOrder', primary_key=True)  # Field name made lowercase.
    groupedorders = models.CharField(db_column='groupedOrders', max_length=191, blank=True, null=True)  # Field name made lowercase.
    iduserecommerce = models.IntegerField(db_column='idUserEcommerce', blank=True, null=True)  # Field name made lowercase.
    idecommerceorder = models.CharField(db_column='idEcommerceOrder', max_length=40, blank=True, null=True)  # Field name made lowercase.
    idecommerceorder2 = models.BigIntegerField(db_column='idEcommerceOrder2', blank=True, null=True)  # Field name made lowercase.
    idecommerceproduct = models.CharField(db_column='idEcommerceProduct', max_length=40, blank=True, null=True)  # Field name made lowercase.
    idecommerceitem = models.BigIntegerField(db_column='idEcommerceItem', blank=True, null=True)  # Field name made lowercase.
    totalecommerceorderitems = models.IntegerField(db_column='totalEcommerceOrderItems', blank=True, null=True)  # Field name made lowercase.
    counterecommerceorderitems = models.IntegerField(db_column='counterEcommerceOrderItems', blank=True, null=True)  # Field name made lowercase.
    idlocationecommerce = models.CharField(db_column='idLocationEcommerce', max_length=191, blank=True, null=True)  # Field name made lowercase.
    idmultipayment = models.IntegerField(db_column='idMultiPayment', blank=True, null=True)  # Field name made lowercase.
    ispro = models.IntegerField(db_column='isPro')  # Field name made lowercase.
    isapiorder = models.IntegerField(db_column='isApiOrder')  # Field name made lowercase.
    ismultipackages = models.IntegerField(db_column='isMultiPackages')  # Field name made lowercase.
    isadvances = models.IntegerField(db_column='isAdvances')  # Field name made lowercase.
    numberofpackages = models.IntegerField(db_column='numberOfPackages')  # Field name made lowercase.
    prefquotation = models.CharField(db_column='prefQuotation', max_length=12, blank=True, null=True)  # Field name made lowercase.
    isquoted = models.IntegerField(db_column='isQuoted', blank=True, null=True)  # Field name made lowercase.
    isreadytopay = models.IntegerField(db_column='isReadyToPay')  # Field name made lowercase.
    proguidegenerated = models.IntegerField(db_column='proGuideGenerated', blank=True, null=True)  # Field name made lowercase.
    myreference = models.CharField(db_column='myReference', max_length=28, blank=True, null=True)  # Field name made lowercase.
    usertype = models.IntegerField(db_column='userType', blank=True, null=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='firstName', max_length=150)  # Field name made lowercase.
    lastname = models.CharField(db_column='lastName', max_length=150)  # Field name made lowercase.
    email = models.CharField(max_length=250)
    description = models.CharField(max_length=255, blank=True, null=True)
    contentvalue = models.DecimalField(db_column='contentValue', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    insuredamount = models.FloatField(db_column='insuredAmount', blank=True, null=True)  # Field name made lowercase.
    discountcoupon = models.CharField(db_column='discountCoupon', max_length=100, blank=True, null=True)  # Field name made lowercase.
    discountamount = models.CharField(db_column='discountAmount', max_length=45, blank=True, null=True)  # Field name made lowercase.
    service = models.CharField(max_length=255, blank=True, null=True)
    pickupdate = models.DateField(db_column='pickupDate', blank=True, null=True)  # Field name made lowercase.
    pickupschedule = models.IntegerField(db_column='pickupSchedule', blank=True, null=True)  # Field name made lowercase.
    info_status = models.CharField(max_length=14, blank=True, null=True)
    paid = models.IntegerField()
    localityfrom = models.CharField(db_column='localityFrom', max_length=150, blank=True, null=True)  # Field name made lowercase.
    localityto = models.CharField(db_column='localityTo', max_length=150, blank=True, null=True)  # Field name made lowercase.
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    cost = models.FloatField(blank=True, null=True)
    carrierrate = models.FloatField(db_column='carrierRate', blank=True, null=True)  # Field name made lowercase.
    ratecurrency = models.CharField(db_column='rateCurrency', max_length=4, blank=True, null=True)  # Field name made lowercase.
    remotezonecharge = models.FloatField(db_column='remoteZoneCharge', blank=True, null=True)  # Field name made lowercase.
    tax = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    insurance = models.IntegerField(blank=True, null=True)
    amountinsurance = models.FloatField(db_column='amountInsurance', blank=True, null=True)  # Field name made lowercase.
    amountinsurancews = models.FloatField(db_column='amountInsuranceWS', blank=True, null=True)  # Field name made lowercase.
    trackingcode = models.CharField(db_column='trackingCode', max_length=40, blank=True, null=True)  # Field name made lowercase.
    trackingcodeinternal = models.CharField(db_column='trackingCodeInternal', max_length=40, blank=True, null=True)  # Field name made lowercase.
    idcarrier = models.IntegerField(db_column='idCarrier', blank=True, null=True)  # Field name made lowercase.
    guia = models.TextField(blank=True, null=True)
    idorderstatus = models.ForeignKey(OrderStatus, models.DO_NOTHING, db_column='idOrderStatus')  # Field name made lowercase.
    iduser = models.ForeignKey('Users', models.DO_NOTHING, db_column='idUser')  # Field name made lowercase.
    idcoupon = models.ForeignKey(Coupons, models.DO_NOTHING, db_column='idCoupon', blank=True, null=True)  # Field name made lowercase.
    idrate = models.ForeignKey('Rates', models.DO_NOTHING, db_column='idRate', blank=True, null=True)  # Field name made lowercase.
    idratemultipackages = models.IntegerField(db_column='idRateMultiPackages', blank=True, null=True)  # Field name made lowercase.
    idcashback = models.IntegerField(db_column='idCashback', blank=True, null=True)  # Field name made lowercase.
    idaddressshipper = models.IntegerField(db_column='idAddressShipper', blank=True, null=True)  # Field name made lowercase.
    sendercompany = models.CharField(db_column='senderCompany', max_length=28, blank=True, null=True)  # Field name made lowercase.
    senderfirstname = models.CharField(db_column='senderFirstName', max_length=150)  # Field name made lowercase.
    senderlastname = models.CharField(db_column='senderLastName', max_length=150)  # Field name made lowercase.
    senderemail = models.CharField(db_column='senderEmail', max_length=250)  # Field name made lowercase.
    senderphone = models.CharField(db_column='senderPhone', max_length=12)  # Field name made lowercase.
    senderaddress1 = models.CharField(db_column='senderAddress1', max_length=250)  # Field name made lowercase.
    sendernumber = models.CharField(db_column='senderNumber', max_length=10, blank=True, null=True)  # Field name made lowercase.
    sendercolonia = models.CharField(db_column='senderColonia', max_length=250, blank=True, null=True)  # Field name made lowercase.
    sendercrossstreet = models.CharField(db_column='senderCrossStreet', max_length=35, blank=True, null=True)  # Field name made lowercase.
    senderreference = models.CharField(db_column='senderReference', max_length=250, blank=True, null=True)  # Field name made lowercase.
    senderzip = models.CharField(db_column='senderZip', max_length=6)  # Field name made lowercase.
    senderlocality = models.CharField(db_column='senderLocality', max_length=150)  # Field name made lowercase.
    senderstate = models.CharField(db_column='senderState', max_length=150)  # Field name made lowercase.
    sendercountry = models.CharField(db_column='senderCountry', max_length=150)  # Field name made lowercase.
    senderlat = models.FloatField(db_column='senderLat', blank=True, null=True)  # Field name made lowercase.
    senderlng = models.FloatField(db_column='senderLng', blank=True, null=True)  # Field name made lowercase.
    idaddressrecipient = models.IntegerField(db_column='idAddressRecipient', blank=True, null=True)  # Field name made lowercase.
    addresseecompany = models.CharField(db_column='addresseeCompany', max_length=28, blank=True, null=True)  # Field name made lowercase.
    addresseefirstname = models.CharField(db_column='addresseeFirstName', max_length=150)  # Field name made lowercase.
    addresseelastname = models.CharField(db_column='addresseeLastName', max_length=150)  # Field name made lowercase.
    addresseeemail = models.CharField(db_column='addresseeEmail', max_length=250)  # Field name made lowercase.
    addresseephone = models.CharField(db_column='addresseePhone', max_length=12)  # Field name made lowercase.
    addresseeaddress1 = models.CharField(db_column='addresseeAddress1', max_length=250)  # Field name made lowercase.
    addresseenumber = models.CharField(db_column='addresseeNumber', max_length=10, blank=True, null=True)  # Field name made lowercase.
    addresseecolonia = models.CharField(db_column='addresseeColonia', max_length=250, blank=True, null=True)  # Field name made lowercase.
    addresseecrossstreet = models.CharField(db_column='addresseeCrossStreet', max_length=35, blank=True, null=True)  # Field name made lowercase.
    addresseereference = models.CharField(db_column='addresseeReference', max_length=250, blank=True, null=True)  # Field name made lowercase.
    addresseezip = models.CharField(db_column='addresseeZip', max_length=6)  # Field name made lowercase.
    addresseelocality = models.CharField(db_column='addresseeLocality', max_length=150)  # Field name made lowercase.
    addresseestate = models.CharField(db_column='addresseeState', max_length=150)  # Field name made lowercase.
    addresseecountry = models.CharField(db_column='addresseeCountry', max_length=150)  # Field name made lowercase.
    addresseelat = models.FloatField(db_column='addresseeLat', blank=True, null=True)  # Field name made lowercase.
    addresseelng = models.FloatField(db_column='addresseeLng', blank=True, null=True)  # Field name made lowercase.
    invoicerfc = models.CharField(db_column='invoiceRFC', max_length=30)  # Field name made lowercase.
    invoicecompany = models.CharField(db_column='invoiceCompany', max_length=255)  # Field name made lowercase.
    invoicefirstname = models.CharField(db_column='invoiceFirstName', max_length=150)  # Field name made lowercase.
    invoicelastname = models.CharField(db_column='invoiceLastName', max_length=150)  # Field name made lowercase.
    invoiceemail = models.CharField(db_column='invoiceEmail', max_length=250)  # Field name made lowercase.
    invoicephone = models.CharField(db_column='invoicePhone', max_length=12)  # Field name made lowercase.
    invoiceaddress1 = models.CharField(db_column='invoiceAddress1', max_length=250)  # Field name made lowercase.
    invoicecolonia = models.CharField(db_column='invoiceColonia', max_length=250, blank=True, null=True)  # Field name made lowercase.
    invoicezip = models.CharField(db_column='invoiceZip', max_length=6)  # Field name made lowercase.
    invoicelocality = models.CharField(db_column='invoiceLocality', max_length=150)  # Field name made lowercase.
    invoicestate = models.CharField(db_column='invoiceState', max_length=150)  # Field name made lowercase.
    invoicecountry = models.CharField(db_column='invoiceCountry', max_length=150)  # Field name made lowercase.
    carrierinvoiceweight = models.FloatField(db_column='carrierInvoiceWeight', blank=True, null=True)  # Field name made lowercase.
    carrierinvoicerate = models.FloatField(db_column='carrierInvoiceRate', blank=True, null=True)  # Field name made lowercase.
    carrierinvoicetotal = models.FloatField(db_column='carrierInvoiceTotal', blank=True, null=True)  # Field name made lowercase.
    paymentmethod = models.CharField(db_column='paymentMethod', max_length=50, blank=True, null=True)  # Field name made lowercase.
    paymentcommissionpercentage = models.FloatField(db_column='paymentCommissionPercentage', blank=True, null=True)  # Field name made lowercase.
    paymentcommissionfixed = models.FloatField(db_column='paymentCommissionFixed', blank=True, null=True)  # Field name made lowercase.
    paymentcommissiontotal = models.FloatField(db_column='paymentCommissionTotal', blank=True, null=True)  # Field name made lowercase.
    paymentday = models.DateTimeField(db_column='paymentDay', blank=True, null=True)  # Field name made lowercase.
    paymentreference = models.CharField(db_column='paymentReference', max_length=45, blank=True, null=True)  # Field name made lowercase.
    pickup = models.IntegerField()
    pickupid = models.CharField(db_column='pickupID', max_length=18, blank=True, null=True)  # Field name made lowercase.
    invoiceticket = models.IntegerField(db_column='invoiceTicket')  # Field name made lowercase.
    canceled = models.IntegerField()
    cancellation_reason = models.CharField(max_length=255, blank=True, null=True)
    cancellation_date = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    deleted_at = models.DateTimeField(blank=True, null=True)
    statusec = models.CharField(db_column='statusEc', max_length=120, blank=True, null=True)  # Field name made lowercase.
    statusclient = models.CharField(db_column='statusClient', max_length=120, blank=True, null=True)  # Field name made lowercase.
    incidence = models.IntegerField(blank=True, null=True)
    incidencetype = models.CharField(db_column='incidenceType', max_length=40, blank=True, null=True)  # Field name made lowercase.
    statusstep = models.CharField(db_column='statusStep', max_length=45, blank=True, null=True)  # Field name made lowercase.
    intransitnotificationdelivered = models.IntegerField(db_column='inTransitNotificationDelivered')  # Field name made lowercase.
    arrivaldate = models.DateField(db_column='arrivalDate', blank=True, null=True)  # Field name made lowercase.
    isdownloadguide = models.IntegerField(db_column='isDownloadGuide')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'orders'


class PProfile(models.Model):
    idprofile = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'p_profile'


class Packaging(models.Model):
    idpacking = models.AutoField(db_column='idPacking', primary_key=True)  # Field name made lowercase.
    iduser = models.IntegerField(db_column='idUser')  # Field name made lowercase.
    name = models.CharField(max_length=30)
    length = models.FloatField()
    width = models.FloatField()
    height = models.FloatField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'packaging'


# class PasswordResets(models.Model):
#     email = models.CharField(max_length=191)
#     token = models.CharField(max_length=191)
#     created_at = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'password_resets'


# class PaymentErrors(models.Model):
#     reference = models.CharField(max_length=191)
#     platform = models.CharField(max_length=191)
#     type = models.CharField(max_length=191)
#     idorders = models.CharField(db_column='idOrders', max_length=191, blank=True, null=True)  # Field name made lowercase.
#     total = models.DecimalField(max_digits=11, decimal_places=2)
#     iduser = models.IntegerField(db_column='idUser')  # Field name made lowercase.
#     created_at = models.DateTimeField(blank=True, null=True)
#     updated_at = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'payment_errors'


class PaymentMethods(models.Model):
    idpaymentmethod = models.AutoField(db_column='idPaymentMethod', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=45)
    environment = models.CharField(max_length=18)
    available = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'payment_methods'


# class PaymentsLog(models.Model):
#     iduser = models.IntegerField(db_column='idUser')  # Field name made lowercase.
#     paymenttype = models.CharField(db_column='paymentType', max_length=191)  # Field name made lowercase.
#     message = models.CharField(max_length=191)
#     status = models.CharField(max_length=191)
#     request = models.TextField()
#     paymentresponse = models.TextField(db_column='paymentResponse')  # Field name made lowercase.
#     created_at = models.DateTimeField(blank=True, null=True)
#     updated_at = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'payments_log'


# class PickupTries(models.Model):
#     idpickup = models.IntegerField(db_column='idPickup')  # Field name made lowercase.
#     idreason = models.IntegerField(db_column='idReason')  # Field name made lowercase.
#     date = models.DateTimeField()
#     isfinal = models.IntegerField(db_column='isFinal')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'pickup_tries'


class Pickups(models.Model):
    idpickup = models.AutoField(db_column='idPickup', primary_key=True)  # Field name made lowercase.
    pickup_date = models.DateTimeField()
    status = models.IntegerField()
    idcarrier = models.IntegerField(db_column='idCarrier')  # Field name made lowercase.
    idproduct = models.IntegerField(db_column='idProduct', blank=True, null=True)  # Field name made lowercase.
    idorder = models.IntegerField(db_column='idOrder', blank=True, null=True)  # Field name made lowercase.
    iduser = models.IntegerField(db_column='idUser', blank=True, null=True)  # Field name made lowercase.
    firstname = models.CharField(max_length=150, blank=True, null=True)
    lastname = models.CharField(max_length=150, blank=True, null=True)
    email = models.CharField(max_length=150, blank=True, null=True)
    phone = models.CharField(max_length=18, blank=True, null=True)
    address = models.CharField(max_length=150)
    number = models.CharField(max_length=5, blank=True, null=True)
    locality = models.CharField(max_length=150, blank=True, null=True)
    colonia = models.CharField(max_length=150, blank=True, null=True)
    zipcode = models.CharField(max_length=6)
    state = models.CharField(max_length=40, blank=True, null=True)
    crossstreet = models.CharField(db_column='crossStreet', max_length=35, blank=True, null=True)  # Field name made lowercase.
    reference = models.CharField(max_length=45, blank=True, null=True)
    pickup_id = models.CharField(max_length=45, blank=True, null=True)
    error_ws = models.CharField(max_length=120, blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pickups'


class ProductDiscountLog(models.Model):
    idproductdiscountlog = models.AutoField(db_column='idProductDiscountLog', primary_key=True)  # Field name made lowercase.
    idproduct = models.IntegerField(db_column='idProduct')  # Field name made lowercase.
    iduser = models.IntegerField(db_column='idUser')  # Field name made lowercase.
    olddiscount = models.FloatField(db_column='oldDiscount')  # Field name made lowercase.
    newdiscount = models.FloatField(db_column='newDiscount')  # Field name made lowercase.
    created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'product_discount_log'


class Products(models.Model):
    idproduct = models.AutoField(db_column='idProduct', primary_key=True)  # Field name made lowercase.
    idcarrier = models.ForeignKey(Carriers, models.DO_NOTHING, db_column='idCarrier')  # Field name made lowercase.
    servicetypeid = models.CharField(db_column='serviceTypeId', max_length=18, blank=True, null=True)  # Field name made lowercase.
    code = models.CharField(max_length=45)
    wscode = models.CharField(db_column='wsCode', max_length=42, blank=True, null=True)  # Field name made lowercase.
    product = models.CharField(max_length=200)
    url = models.CharField(max_length=50)
    description = models.CharField(max_length=500, blank=True, null=True)
    available = models.IntegerField()
    trackable = models.IntegerField()
    terms = models.TextField()
    daysmin = models.IntegerField(db_column='daysMin', blank=True, null=True)  # Field name made lowercase.
    days = models.FloatField(blank=True, null=True)
    delayofdays = models.IntegerField(db_column='delayOfDays')  # Field name made lowercase.
    arrivesatmin = models.TimeField(db_column='arrivesAtMin', blank=True, null=True)  # Field name made lowercase.
    arrivesatfrom = models.TimeField(db_column='arrivesAtFrom', blank=True, null=True)  # Field name made lowercase.
    arrivesat = models.TimeField(db_column='arrivesAt')  # Field name made lowercase.
    discount = models.FloatField(blank=True, null=True)
    orderhourlimit = models.TimeField(db_column='orderHourLimit')  # Field name made lowercase.
    outboundendpoint = models.IntegerField()
    inboundendpoint = models.IntegerField()
    created = models.DateTimeField()
    modified = models.DateTimeField()
    weightincluded = models.FloatField(db_column='weightIncluded', blank=True, null=True)  # Field name made lowercase.
    weightmax = models.FloatField(db_column='weightMax', blank=True, null=True)  # Field name made lowercase.
    widthmax = models.FloatField(db_column='widthMax', blank=True, null=True)  # Field name made lowercase.
    heightmax = models.FloatField(db_column='heightMax', blank=True, null=True)  # Field name made lowercase.
    widemax = models.FloatField(db_column='wideMax', blank=True, null=True)  # Field name made lowercase.
    saturdaycollectionoverprice = models.FloatField(db_column='saturdayCollectionOverprice', blank=True, null=True)  # Field name made lowercase.
    remotezonecollectionoverprice = models.FloatField(db_column='remoteZoneCollectionOverprice', blank=True, null=True)  # Field name made lowercase.
    remotezonedeliveryoverprice = models.FloatField(db_column='remoteZoneDeliveryOverprice', blank=True, null=True)  # Field name made lowercase.
    multipackageoverprice = models.FloatField(db_column='multipackageOverprice', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'products'


# class RateTypes(models.Model):
#     type = models.CharField(max_length=191)
#     description = models.CharField(max_length=191)

#     class Meta:
#         managed = False
#         db_table = 'rate_types'


class Rates(models.Model):
    idrate = models.AutoField(db_column='idRate', primary_key=True)  # Field name made lowercase.
    idzone = models.ForeignKey('Zones', models.DO_NOTHING, db_column='idZone')  # Field name made lowercase.
    idproduct = models.ForeignKey(Products, models.DO_NOTHING, db_column='idProduct')  # Field name made lowercase.
    ratetype = models.IntegerField(db_column='rateType')  # Field name made lowercase.
    weight_min = models.DecimalField(max_digits=6, decimal_places=2)
    weight_max = models.DecimalField(max_digits=6, decimal_places=2)
    carrierrate = models.FloatField(db_column='carrierRate', blank=True, null=True)  # Field name made lowercase.
    overweightcarrierrate = models.FloatField(db_column='overweightCarrierRate', blank=True, null=True)  # Field name made lowercase.
    price = models.DecimalField(max_digits=10, decimal_places=2)
    overweight = models.FloatField(blank=True, null=True)
    cost = models.FloatField(blank=True, null=True)
    overweightcost = models.FloatField(db_column='overweightCost', blank=True, null=True)  # Field name made lowercase.
    fuelcharge = models.FloatField(db_column='fuelCharge', blank=True, null=True)  # Field name made lowercase.
    remotezonecharge = models.FloatField(db_column='remoteZoneCharge', blank=True, null=True)  # Field name made lowercase.
    specialremotezonecharge = models.FloatField(db_column='specialRemoteZoneCharge')  # Field name made lowercase.
    fee = models.DecimalField(max_digits=10, decimal_places=2)
    vehicle_type = models.CharField(max_length=45, blank=True, null=True)
    ratedescription = models.CharField(db_column='rateDescription', max_length=150, blank=True, null=True)  # Field name made lowercase.
    isocurre = models.CharField(db_column='isOcurre', max_length=191)  # Field name made lowercase.
    daystodeliver = models.IntegerField(db_column='daysToDeliver', blank=True, null=True)  # Field name made lowercase.
    datedeliverypromise = models.DateTimeField(db_column='dateDeliveryPromise', blank=True, null=True)  # Field name made lowercase.
    ratecurrency = models.CharField(db_column='rateCurrency', max_length=4)  # Field name made lowercase.
    weight = models.FloatField(blank=True, null=True)
    length = models.FloatField(blank=True, null=True)
    width = models.FloatField(blank=True, null=True)
    height = models.FloatField(blank=True, null=True)
    totaldays = models.IntegerField(db_column='totalDays', blank=True, null=True)  # Field name made lowercase.
    senderzip = models.CharField(db_column='senderZip', max_length=6, blank=True, null=True)  # Field name made lowercase.
    addresseezip = models.CharField(db_column='addresseeZip', max_length=6, blank=True, null=True)  # Field name made lowercase.
    available = models.IntegerField()
    isadvances = models.IntegerField(db_column='isAdvances')  # Field name made lowercase.
    iduser = models.IntegerField(db_column='idUser', blank=True, null=True)  # Field name made lowercase.
    created = models.DateTimeField()
    modified = models.DateTimeField()
    max_volume = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    min_volume = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rates'


class Ratesmultipackages(models.Model):
    idrate = models.AutoField(db_column='idRate', primary_key=True)  # Field name made lowercase.
    idproduct = models.IntegerField(db_column='idProduct')  # Field name made lowercase.
    carrierrate = models.FloatField(db_column='carrierRate')  # Field name made lowercase.
    price = models.FloatField()
    cost = models.FloatField()
    weight = models.TextField()
    length = models.TextField()
    width = models.TextField()
    height = models.TextField()
    senderzip = models.CharField(db_column='senderZip', max_length=191)  # Field name made lowercase.
    addresseezip = models.CharField(db_column='addresseeZip', max_length=191)  # Field name made lowercase.
    totaldays = models.IntegerField(db_column='totalDays')  # Field name made lowercase.
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ratesMultiPackages'


class Reasons(models.Model):
    idreason = models.AutoField(db_column='idReason', primary_key=True)  # Field name made lowercase.
    reason = models.CharField(max_length=60)
    type = models.CharField(max_length=24)

    class Meta:
        managed = False
        db_table = 'reasons'


class Sessions(models.Model):
    id = models.CharField(unique=True, max_length=191, primary_key=True)
    user_id = models.IntegerField(blank=True, null=True)
    ip_address = models.CharField(max_length=45, blank=True, null=True)
    user_agent = models.TextField(blank=True, null=True)
    payload = models.TextField()
    last_activity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sessions'


class Settlement(models.Model):
    idsettlement = models.AutoField(primary_key=True)
    idzipcode = models.IntegerField(db_column='idZipCode')  # Field name made lowercase.
    settlementtype = models.CharField(db_column='settlementType', max_length=64, blank=True, null=True)  # Field name made lowercase.
    settlementtypeabbr = models.CharField(db_column='settlementTypeAbbr', max_length=16, blank=True, null=True)  # Field name made lowercase.
    settlementname = models.CharField(db_column='settlementName', max_length=128)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'settlement'


class SettlementType(models.Model):
    idsettlementtype = models.AutoField(db_column='idSettlementType', primary_key=True)  # Field name made lowercase.
    abbreviation = models.CharField(max_length=10, blank=True, null=True)
    description = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'settlement_type'


# class SpecialLog(models.Model):
#     file = models.CharField(max_length=45)
#     line = models.CharField(max_length=45)
#     variable = models.CharField(max_length=45)
#     spected = models.CharField(max_length=45)
#     value = models.TextField()
#     idclient = models.IntegerField(db_column='idClient', blank=True, null=True)  # Field name made lowercase.
#     idorder = models.IntegerField(db_column='idOrder', blank=True, null=True)  # Field name made lowercase.
#     idrate = models.IntegerField(db_column='idRate', blank=True, null=True)  # Field name made lowercase.
#     created = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'special_log'


class States(models.Model):
    idstate = models.AutoField(db_column='idState', primary_key=True)  # Field name made lowercase.
    state = models.CharField(max_length=150)
    idcountry = models.ForeignKey(Countries, models.DO_NOTHING, db_column='idCountry')  # Field name made lowercase.
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'states'


class StatusMapping(models.Model):
    idstatusmapping = models.AutoField(db_column='idStatusMapping', primary_key=True)  # Field name made lowercase.
    idcarrier = models.IntegerField(db_column='idCarrier')  # Field name made lowercase.
    statusec = models.CharField(db_column='statusEc', max_length=120)  # Field name made lowercase.
    statusclient = models.CharField(db_column='statusClient', max_length=120)  # Field name made lowercase.
    incidence = models.IntegerField()
    incidencetype = models.CharField(db_column='incidenceType', max_length=40, blank=True, null=True)  # Field name made lowercase.
    status1 = models.CharField(max_length=255)
    status2 = models.CharField(max_length=255, blank=True, null=True)
    undefined = models.IntegerField()
    statusstep = models.CharField(db_column='statusStep', max_length=45)  # Field name made lowercase.
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'status_mapping'


# class TempCsv(models.Model):
#     iduser = models.IntegerField(db_column='idUser', blank=True, null=True)  # Field name made lowercase.
#     shipments = models.TextField()
#     warnings = models.TextField()
#     created = models.DateTimeField()
#     modified = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'temp_csv'


class TempMultipackagesHistory(models.Model):
    idorderhistory = models.AutoField(db_column='idorderHistory', primary_key=True)  # Field name made lowercase.
    idorder = models.IntegerField(db_column='idOrder')  # Field name made lowercase.
    packages = models.IntegerField()
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'temp_multiPackages_history'


# class TrackingLog(models.Model):
#     idorder = models.CharField(db_column='idOrder', max_length=45, blank=True, null=True)  # Field name made lowercase.
#     carrier = models.CharField(max_length=45, blank=True, null=True)
#     trackingcode = models.CharField(db_column='trackingCode', max_length=45, blank=True, null=True)  # Field name made lowercase.
#     request = models.TextField(blank=True, null=True)
#     response = models.TextField(blank=True, null=True)
#     responsejson = models.TextField(db_column='responseJson', blank=True, null=True)  # Field name made lowercase.
#     status1 = models.CharField(max_length=45, blank=True, null=True)
#     statuscode1 = models.CharField(db_column='statusCode1', max_length=45, blank=True, null=True)  # Field name made lowercase.
#     statusdescription1 = models.CharField(db_column='statusDescription1', max_length=120, blank=True, null=True)  # Field name made lowercase.
#     status2 = models.CharField(max_length=45, blank=True, null=True)
#     statuscode2 = models.CharField(db_column='statusCode2', max_length=45, blank=True, null=True)  # Field name made lowercase.
#     statusdescription2 = models.CharField(db_column='statusDescription2', max_length=120, blank=True, null=True)  # Field name made lowercase.
#     additional = models.TextField(blank=True, null=True)
#     orderdate = models.DateTimeField(db_column='orderDate', blank=True, null=True)  # Field name made lowercase.
#     logdate = models.DateTimeField(db_column='logDate', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'tracking_log'


class UserActivations(models.Model):
    iduseractivation = models.AutoField(db_column='idUserActivation', primary_key=True)  # Field name made lowercase.
    iduser = models.IntegerField(db_column='idUser')  # Field name made lowercase.
    token = models.CharField(max_length=191)
    created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_activations'


# class UserAssignmentsToGroups(models.Model):
#     iduser = models.IntegerField(db_column='idUser')  # Field name made lowercase.
#     idusergroup = models.IntegerField(db_column='idUserGroup')  # Field name made lowercase.
#     movement = models.IntegerField()
#     created = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'user_assignments_to_groups'


class UserBackend(models.Model):
    iduserbackend = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    idprofile = models.ForeignKey(PProfile, models.DO_NOTHING, db_column='idprofile')
    remember_token = models.CharField(max_length=100, blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_backend'


class UserBrand(models.Model):
    iduserbrand = models.AutoField(db_column='idUserBrand', primary_key=True)  # Field name made lowercase.
    iduser = models.ForeignKey('Users', models.DO_NOTHING, db_column='idUser')  # Field name made lowercase.
    name = models.CharField(max_length=50, blank=True, null=True)
    active = models.IntegerField()
    website = models.CharField(max_length=100, blank=True, null=True)
    logo = models.CharField(max_length=191, blank=True, null=True)
    color = models.CharField(max_length=15, blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_brand'


class UserCarriers(models.Model):
    idusercarrier = models.AutoField(db_column='idUserCarrier', primary_key=True)  # Field name made lowercase.
    iduser = models.IntegerField(db_column='idUser')  # Field name made lowercase.
    idcarrier = models.IntegerField(db_column='idCarrier')  # Field name made lowercase.
    carrier = models.CharField(max_length=40)
    status = models.CharField(max_length=40)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_carriers'


class UserConfig99Min(models.Model):
    idconfig99min = models.AutoField(db_column='idConfig99min', primary_key=True)  # Field name made lowercase.
    iduser = models.ForeignKey('Users', models.DO_NOTHING, db_column='idUser')  # Field name made lowercase.
    api_key = models.CharField(max_length=191)
    user_id = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_config99min'


class UserConfigaeroflash(models.Model):
    idconfigaeroflash = models.AutoField(db_column='idConfigAeroflash', primary_key=True)  # Field name made lowercase.
    iduser = models.ForeignKey('Users', models.DO_NOTHING, db_column='idUser')  # Field name made lowercase.
    user = models.CharField(max_length=191)
    password = models.CharField(max_length=191)
    contract = models.CharField(max_length=191)
    num_client = models.CharField(max_length=191)
    clave_servicio = models.CharField(max_length=191)
    token = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_configAeroflash'


class UserConfigdhl(models.Model):
    idconfigdhl = models.AutoField(db_column='idConfigDhl', primary_key=True)  # Field name made lowercase.
    iduser = models.ForeignKey('Users', models.DO_NOTHING, db_column='idUser')  # Field name made lowercase.
    account_number = models.CharField(max_length=191)
    site_id = models.CharField(max_length=191)
    password = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_configDhl'


class UserConfigestafeta(models.Model):
    idconfigestafeta = models.AutoField(db_column='idConfigEstafeta', primary_key=True)  # Field name made lowercase.
    iduser = models.ForeignKey('Users', models.DO_NOTHING, db_column='idUser')  # Field name made lowercase.
    shipment_client = models.CharField(max_length=191)
    shipment_office_num = models.CharField(max_length=191)
    shipment_suscriber_id = models.CharField(max_length=191)
    shipment_user = models.CharField(max_length=191)
    shipment_password = models.CharField(max_length=191)
    rate_id_user = models.CharField(max_length=191)
    rate_user = models.CharField(max_length=191)
    rate_password = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_configEstafeta'


class UserConfigfedex(models.Model):
    idconfigfedex = models.AutoField(db_column='idConfigFedex', primary_key=True)  # Field name made lowercase.
    iduser = models.ForeignKey('Users', models.DO_NOTHING, db_column='idUser')  # Field name made lowercase.
    account_number = models.CharField(max_length=191)
    key = models.CharField(max_length=191)
    meter_number = models.CharField(max_length=191)
    password = models.CharField(max_length=191)
    threshold_account_number = models.CharField(max_length=191)
    threshold_key = models.CharField(max_length=191)
    threshold_meter_number = models.CharField(max_length=191)
    threshold_password = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_configFedex'


class UserConfigredpack(models.Model):
    idconfigredpack = models.AutoField(db_column='idConfigRedpack', primary_key=True)  # Field name made lowercase.
    iduser = models.ForeignKey('Users', models.DO_NOTHING, db_column='idUser')  # Field name made lowercase.
    pin = models.CharField(max_length=191)
    user_id = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_configRedpack'


class UserCredit(models.Model):
    idusercredit = models.AutoField(db_column='idUserCredit', primary_key=True)  # Field name made lowercase.
    iduserbackend = models.IntegerField(db_column='idUserBackend')  # Field name made lowercase.
    iduser = models.ForeignKey('Users', models.DO_NOTHING, db_column='idUser')  # Field name made lowercase.
    idmultipayment = models.IntegerField(db_column='idMultiPayment', blank=True, null=True)  # Field name made lowercase.
    idusercreditbonus = models.IntegerField(db_column='idUserCreditBonus', blank=True, null=True)  # Field name made lowercase.
    type = models.IntegerField()
    amount = models.FloatField(blank=True, null=True)
    paymentmethod = models.CharField(db_column='paymentMethod', max_length=45, blank=True, null=True)  # Field name made lowercase.
    paymentreference = models.CharField(db_column='paymentReference', max_length=45, blank=True, null=True)  # Field name made lowercase.
    idorder = models.ForeignKey(Orders, models.DO_NOTHING, db_column='idOrder', blank=True, null=True)  # Field name made lowercase.
    idcashback = models.IntegerField(db_column='idCashback', blank=True, null=True)  # Field name made lowercase.
    reason = models.CharField(max_length=255, blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField(blank=True, null=True)
    file = models.CharField(max_length=38, blank=True, null=True)
    transferid = models.CharField(db_column='transferID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    isloss = models.IntegerField(db_column='isLoss', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user_credit'


class UserDetails(models.Model):
    iduserdetail = models.AutoField(db_column='idUserDetail', primary_key=True)  # Field name made lowercase.
    iduser = models.ForeignKey('Users', models.DO_NOTHING, db_column='idUser')  # Field name made lowercase.
    department = models.CharField(max_length=191, blank=True, null=True)
    company = models.CharField(max_length=120, blank=True, null=True)
    issellingonline = models.IntegerField(db_column='isSellingOnline', blank=True, null=True)  # Field name made lowercase.
    estimatedmaxticketsamount = models.CharField(db_column='estimatedMaxTicketsAmount', max_length=18, blank=True, null=True)  # Field name made lowercase.
    businesscategory = models.CharField(db_column='businessCategory', max_length=40, blank=True, null=True)  # Field name made lowercase.
    taxsituation = models.CharField(db_column='taxSituation', max_length=40, blank=True, null=True)  # Field name made lowercase.
    website = models.CharField(max_length=120, blank=True, null=True)
    projecttype = models.CharField(db_column='projectType', max_length=40, blank=True, null=True)  # Field name made lowercase.
    ecommerce = models.CharField(max_length=40, blank=True, null=True)
    marketplace = models.CharField(max_length=40, blank=True, null=True)
    customsystem = models.CharField(db_column='customSystem', max_length=40, blank=True, null=True)  # Field name made lowercase.
    language = models.CharField(max_length=40, blank=True, null=True)
    tradename = models.CharField(max_length=120, blank=True, null=True)
    facebook = models.CharField(max_length=180, blank=True, null=True)
    inactivecarriers = models.CharField(db_column='inactiveCarriers', max_length=120, blank=True, null=True)  # Field name made lowercase.
    businessname = models.CharField(db_column='businessName', max_length=120, blank=True, null=True)  # Field name made lowercase.
    rfc = models.CharField(max_length=18, blank=True, null=True)
    taxidentificationcard = models.TextField(db_column='taxIdentificationCard', blank=True, null=True)  # Field name made lowercase.
    constitutiveact = models.TextField(db_column='constitutiveAct', blank=True, null=True)  # Field name made lowercase.
    phonefiscal = models.CharField(db_column='phoneFiscal', max_length=18, blank=True, null=True)  # Field name made lowercase.
    idfiscaladdress = models.IntegerField(db_column='idFiscalAddress', blank=True, null=True)  # Field name made lowercase.
    idreturnaddress = models.IntegerField(db_column='idReturnAddress', blank=True, null=True)  # Field name made lowercase.
    representativename = models.CharField(db_column='representativeName', max_length=180, blank=True, null=True)  # Field name made lowercase.
    representativeidentification = models.TextField(db_column='representativeIdentification', blank=True, null=True)  # Field name made lowercase.
    passport = models.TextField(blank=True, null=True)
    curp = models.TextField(blank=True, null=True)
    producttype1 = models.CharField(db_column='productType1', max_length=60, blank=True, null=True)  # Field name made lowercase.
    producttype2 = models.CharField(db_column='productType2', max_length=60, blank=True, null=True)  # Field name made lowercase.
    producttype3 = models.CharField(db_column='productType3', max_length=60, blank=True, null=True)  # Field name made lowercase.
    commonorigin1 = models.CharField(db_column='commonOrigin1', max_length=120, blank=True, null=True)  # Field name made lowercase.
    commonorigin2 = models.CharField(db_column='commonOrigin2', max_length=120, blank=True, null=True)  # Field name made lowercase.
    commonorigin3 = models.CharField(db_column='commonOrigin3', max_length=120, blank=True, null=True)  # Field name made lowercase.
    commondestination1 = models.CharField(db_column='commonDestination1', max_length=120, blank=True, null=True)  # Field name made lowercase.
    commondestination2 = models.CharField(db_column='commonDestination2', max_length=120, blank=True, null=True)  # Field name made lowercase.
    commondestination3 = models.CharField(db_column='commonDestination3', max_length=120, blank=True, null=True)  # Field name made lowercase.
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_details'


class UserEcommerce(models.Model):
    iduserecommerce = models.AutoField(db_column='idUserEcommerce', primary_key=True)  # Field name made lowercase.
    iduser = models.IntegerField(db_column='idUser')  # Field name made lowercase.
    idecommerce = models.IntegerField(db_column='idEcommerce')  # Field name made lowercase.
    idversion = models.CharField(db_column='idVersion', max_length=120)  # Field name made lowercase.
    url = models.CharField(max_length=120)
    user = models.CharField(max_length=120)
    password = models.CharField(max_length=120)
    wskey = models.CharField(max_length=120)
    company = models.CharField(max_length=28)
    firstname = models.CharField(db_column='firstName', max_length=150)  # Field name made lowercase.
    lastname = models.CharField(db_column='lastName', max_length=150)  # Field name made lowercase.
    email = models.CharField(max_length=250)
    phone = models.CharField(max_length=12)
    address = models.CharField(max_length=250)
    number = models.CharField(max_length=10)
    colonia = models.CharField(max_length=250)
    crossstreet = models.CharField(db_column='crossStreet', max_length=35)  # Field name made lowercase.
    reference = models.CharField(max_length=250)
    zip = models.CharField(max_length=6)
    cotizationorder = models.CharField(db_column='cotizationOrder', max_length=10)  # Field name made lowercase.
    updateecommerce = models.IntegerField(db_column='updateEcommerce')  # Field name made lowercase.
    status = models.IntegerField()
    isvirtual = models.IntegerField(db_column='isVirtual')  # Field name made lowercase.
    usebilling = models.IntegerField(db_column='useBilling')  # Field name made lowercase.
    importingorders = models.IntegerField(db_column='importingOrders')  # Field name made lowercase.
    formshopifytype = models.IntegerField(db_column='formShopifyType')  # Field name made lowercase.
    locationshopify = models.IntegerField(db_column='locationShopify')  # Field name made lowercase.
    statustoimportshopify = models.CharField(db_column='statusToImportShopify', max_length=191)  # Field name made lowercase.
    statuspaymenttoimportshopify = models.CharField(db_column='statusPaymentToImportShopify', max_length=191)  # Field name made lowercase.
    statustoimport = models.CharField(db_column='statusToImport', max_length=191)  # Field name made lowercase.
    lastconnection = models.DateTimeField(db_column='lastConnection')  # Field name made lowercase.
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    access_token_mercadolibre = models.CharField(max_length=191)
    refresh_token_mercadolibre = models.CharField(max_length=191)

    class Meta:
        managed = False
        db_table = 'user_ecommerce'


class UserGroups(models.Model):
    idusergroup = models.AutoField(db_column='idUserGroup', primary_key=True)  # Field name made lowercase.
    idcashback = models.IntegerField(db_column='idCashback', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(max_length=45, blank=True, null=True)
    businessname = models.CharField(db_column='businessName', max_length=125, blank=True, null=True)  # Field name made lowercase.
    rfc = models.CharField(max_length=16, blank=True, null=True)
    description = models.CharField(max_length=256, blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    deleted = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_groups'


class UserLabel(models.Model):
    iduserlabel = models.AutoField(db_column='idUserLabel', primary_key=True)  # Field name made lowercase.
    iduser = models.IntegerField(db_column='idUser')  # Field name made lowercase.
    idcarrier = models.IntegerField(db_column='idCarrier')  # Field name made lowercase.
    idlabel = models.IntegerField(db_column='idLabel')  # Field name made lowercase.
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_label'


class Users(models.Model):
    iduser = models.AutoField(db_column='idUser', primary_key=True)  # Field name made lowercase.
    iddiscount = models.IntegerField(db_column='idDiscount', blank=True, null=True)  # Field name made lowercase.
    miniumiddiscount = models.IntegerField(db_column='miniumIdDiscount', blank=True, null=True)  # Field name made lowercase.
    discountupdatedat = models.DateField(db_column='discountUpdatedAt', blank=True, null=True)  # Field name made lowercase.
    iddealer = models.IntegerField(db_column='idDealer', blank=True, null=True)  # Field name made lowercase.
    idusergroup = models.IntegerField(db_column='idUserGroup', blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(max_length=150, blank=True, null=True)
    email = models.CharField(max_length=250)
    password = models.CharField(max_length=50)
    firstname = models.CharField(max_length=150)
    lastname = models.CharField(max_length=150)
    rfc = models.CharField(max_length=30, blank=True, null=True)
    company = models.CharField(max_length=100, blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    credit = models.FloatField()
    activated = models.IntegerField()
    ispro = models.IntegerField(db_column='isPro')  # Field name made lowercase.
    isvalidpro = models.IntegerField(db_column='isValidPro')  # Field name made lowercase.
    proterms = models.IntegerField(db_column='proTerms')  # Field name made lowercase.
    thermallabel = models.IntegerField(db_column='thermalLabel', blank=True, null=True)  # Field name made lowercase.
    apikey = models.CharField(db_column='apiKey', max_length=45, blank=True, null=True)  # Field name made lowercase.
    changepasswordtoken = models.CharField(db_column='changePasswordToken', max_length=100, blank=True, null=True)  # Field name made lowercase.
    created = models.DateTimeField()
    modified = models.DateTimeField()
    phone = models.CharField(max_length=18)
    remember_token = models.CharField(max_length=100, blank=True, null=True)
    id_conekta_client = models.CharField(max_length=191, blank=True, null=True)
    lockeddiscount = models.IntegerField(db_column='lockedDiscount')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'users'


# class VirketLog(models.Model):
#     idorder = models.IntegerField(db_column='idOrder')  # Field name made lowercase.
#     idproduct = models.IntegerField(db_column='idProduct')  # Field name made lowercase.
#     total = models.FloatField()
#     tax = models.FloatField()
#     price = models.FloatField()
#     paymentmethod = models.CharField(db_column='paymentMethod', max_length=255)  # Field name made lowercase.
#     product = models.CharField(max_length=255)
#     carrier = models.CharField(max_length=255)
#     coupon = models.CharField(max_length=255)
#     texthtml = models.TextField(db_column='textHTML')  # Field name made lowercase.
#     timestamp = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'virket_log'


class Warnings(models.Model):
    idwarning = models.AutoField(db_column='idWarning', primary_key=True)  # Field name made lowercase.
    warning = models.CharField(max_length=60)
    idorder = models.IntegerField(db_column='idOrder', blank=True, null=True)  # Field name made lowercase.
    iduser = models.IntegerField(db_column='idUser', blank=True, null=True)  # Field name made lowercase.
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'warnings'


# class WebhookLogs(models.Model):
#     response = models.TextField()
#     type = models.CharField(max_length=191)
#     platform = models.CharField(max_length=191)
#     created_at = models.DateTimeField(blank=True, null=True)
#     updated_at = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'webhook_logs'


# class WebserviceLog(models.Model):
#     timestamp = models.DateTimeField()
#     sessiondump = models.TextField(db_column='sessionDump', blank=True, null=True)  # Field name made lowercase.
#     environment = models.CharField(max_length=45, blank=True, null=True)
#     endpoint = models.TextField(blank=True, null=True)
#     request = models.TextField(blank=True, null=True)
#     response = models.TextField(blank=True, null=True)
#     exception = models.TextField(blank=True, null=True)
#     message = models.TextField(blank=True, null=True)
#     service = models.CharField(max_length=45, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'webservice_log'


# class WeightAux(models.Model):
#     weight = models.IntegerField(blank=True, null=True)
#     locality = models.CharField(max_length=256, blank=True, null=True)
#     zipcode2 = models.CharField(db_column='zipCode2', max_length=2, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'weight_aux'


# class WsInvoiceLog(models.Model):
#     idorder = models.IntegerField(db_column='idOrder', blank=True, null=True)  # Field name made lowercase.
#     request = models.TextField(blank=True, null=True)
#     response = models.TextField(blank=True, null=True)
#     message = models.CharField(max_length=255, blank=True, null=True)
#     exception = models.TextField(blank=True, null=True)
#     created = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'ws_invoice_log'


class ZipCodes(models.Model):
    idzipcode = models.AutoField(db_column='idZipCode', primary_key=True)  # Field name made lowercase.
    zipcode = models.CharField(db_column='zipCode', max_length=6)  # Field name made lowercase.
    locality = models.CharField(max_length=250)
    idstate = models.ForeignKey(States, models.DO_NOTHING, db_column='idState')  # Field name made lowercase.
    created = models.DateTimeField()
    modified = models.DateTimeField()
    idsettlementtype = models.ForeignKey(SettlementType, models.DO_NOTHING, db_column='idSettlementType', blank=True, null=True)  # Field name made lowercase.
    weight = models.IntegerField(blank=True, null=True)
    af_ocurre = models.IntegerField()
    fx_ocurre = models.IntegerField()
    nnm_ocurre = models.IntegerField()
    rp_ocurre = models.IntegerField()
    est_ocurre = models.IntegerField()
    dhl_ocurre = models.IntegerField()
    tg_ocurre = models.IntegerField()
    plto_ocurre = models.IntegerField()
    pltp_ocurre = models.IntegerField()
    crs_ocurre = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'zip_codes'


class ZipCodesByGroups(models.Model):
    idzipcodebygroup = models.AutoField(db_column='idZipCodeByGroup', primary_key=True)  # Field name made lowercase.
    idzipcode = models.ForeignKey(ZipCodes, models.DO_NOTHING, db_column='idZipCode')  # Field name made lowercase.
    idzipgroup = models.ForeignKey('ZipGroups', models.DO_NOTHING, db_column='idZipGroup')  # Field name made lowercase.
    loaddate = models.DateTimeField(db_column='loadDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'zip_codes_by_groups'


class ZipGroups(models.Model):
    idzipgroup = models.AutoField(db_column='idZipGroup', primary_key=True)  # Field name made lowercase.
    zipgroup = models.CharField(db_column='zipGroup', max_length=30)  # Field name made lowercase.
    idcarrier = models.ForeignKey(Carriers, models.DO_NOTHING, db_column='idCarrier')  # Field name made lowercase.
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'zip_groups'


class Zones(models.Model):
    idzone = models.AutoField(db_column='idZone', primary_key=True)  # Field name made lowercase.
    code = models.CharField(max_length=10)
    zone = models.CharField(max_length=100)
    idcarrier = models.ForeignKey(Carriers, models.DO_NOTHING, db_column='idCarrier')  # Field name made lowercase.
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'zones'
