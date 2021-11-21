from django.db import models


class AltaProd(models.Model):
    noproduccion = models.IntegerField(primary_key=True)
    presup = models.CharField(max_length=15, blank=True, null=True)
    fecha = models.DateTimeField()
    id_productor = models.IntegerField()
    id_realizador = models.IntegerField(blank=True, null=True)
    id_cordinador = models.IntegerField()
    prograb = models.CharField(max_length=1)
    tranvivo = models.CharField(max_length=1)
    materia = models.CharField(max_length=20, blank=True, null=True)
    serie = models.CharField(max_length=80)
    noprogs = models.IntegerField()
    mesrealizacion = models.CharField(max_length=20)
    sinopsis = models.CharField(max_length=300, blank=True, null=True)
    finicio = models.DateTimeField()
    fterminacion = models.DateTimeField()
    observaciones = models.CharField(max_length=400, blank=True, null=True)
    id_firma_dirvin = models.IntegerField(blank=True, null=True)
    id_firma_dirprod = models.IntegerField(blank=True, null=True)
    id_firma_recibemat = models.IntegerField(blank=True, null=True)
    id_tipoprod = models.IntegerField()
    fechap = models.DateTimeField()
    fgrab = models.CharField(max_length=9, blank=True, null=True)
    fmontaje = models.CharField(max_length=9, blank=True, null=True)
    casting = models.IntegerField()
    scouting = models.IntegerField()
    levimagen = models.IntegerField()
    programa = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'alta_prod'


class CalBloques(models.Model):
    vp_id = models.IntegerField()
    id_bloque = models.IntegerField()
    tc_in = models.CharField(max_length=11)
    tc_out = models.CharField(max_length=11)
    duracion = models.CharField(max_length=11)

    class Meta:
        managed = False
        db_table = 'cal_bloques'


class CalContenido(models.Model):
    vp_id = models.IntegerField()
    id_segmento = models.IntegerField()
    id_pregunta = models.IntegerField()
    respuesta = models.CharField(max_length=500)
    fecha = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cal_contenido'


class CalFichatec(models.Model):
    vp_id = models.IntegerField(primary_key=True)
    video = models.IntegerField()
    set_up = models.IntegerField()
    chroma = models.IntegerField()
    drop_out = models.IntegerField()
    desgarres = models.IntegerField()
    rayadas = models.IntegerField()
    hue = models.IntegerField()
    ch_1 = models.IntegerField()
    ch_2 = models.IntegerField()
    falla_ch1 = models.IntegerField()
    falla_ch2 = models.IntegerField()
    c_sonido = models.IntegerField()
    c_audio = models.IntegerField()
    tc_in = models.CharField(max_length=11)
    tc_out = models.CharField(max_length=11)
    duracion = models.CharField(max_length=11)
    lip_sync = models.IntegerField()
    transmision = models.IntegerField()
    motivo_trans = models.CharField(max_length=180, blank=True, null=True)
    observaciones = models.CharField(max_length=300, blank=True, null=True)
    califico = models.CharField(max_length=15)
    fecha = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cal_fichatec'


class CargaMat(models.Model):
    folio_cb = models.CharField(primary_key=True, max_length=12)
    noproduccion = models.IntegerField()
    fprestamo = models.DateTimeField()
    fdevolucion = models.DateTimeField()
    codigobarras = models.CharField(max_length=15, blank=True, null=True)
    form_clave = models.IntegerField()
    id_status = models.CharField(max_length=2)
    id_localizacion = models.IntegerField()
    id_solicitud = models.CharField(max_length=3)
    no_reciclado = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'carga_mat'


class CatArea(models.Model):
    id_area = models.IntegerField()
    area = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'cat_area'


class CatAreac(models.Model):
    id_areac = models.IntegerField()
    areac = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'cat_areac'


class CatLoc(models.Model):
    id_localizacion = models.IntegerField()
    localizacion = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'cat_loc'


class CatNomsubserv(models.Model):
    id_servicio = models.IntegerField()
    id_subserv = models.IntegerField()
    nomsubserv = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'cat_nomsubserv'


class CatServ(models.Model):
    id_servicio = models.IntegerField()
    servicio = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'cat_serv'


class CatStatus(models.Model):
    id_status = models.CharField(max_length=3)
    status = models.CharField(max_length=20)
    abreviacion = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'cat_status'


class CatTipoprod(models.Model):
    id_tipoprod = models.IntegerField(primary_key=True)
    tipoprod = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'cat_tipoprod'


class ControlVideoteca(models.Model):
    id_control = models.IntegerField(primary_key=True)
    fecha = models.DateTimeField()
    sistema = models.CharField(max_length=9)
    movimiento = models.CharField(max_length=16)
    tabla = models.CharField(max_length=19)
    tablakey = models.IntegerField()
    usua_clave = models.CharField(max_length=10)
    bitacora = models.TextField(blank=True, null=True)
    campo = models.TextField(blank=True, null=True)
    programa = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'control_videoteca'


class DetallePrestamos(models.Model):
    pres_folio = models.IntegerField()
    vide_clave = models.IntegerField()
    depr_estatus = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'detalle_prestamos'


class DetalleProgramas(models.Model):
    vp_id = models.IntegerField(primary_key=True)
    video_id = models.IntegerField()
    video_cbarras = models.CharField(max_length=12)
    vp_serie = models.CharField(max_length=300, blank=True, null=True)
    vp_subtitulo = models.CharField(max_length=150, blank=True, null=True)
    vp_sinopsis = models.CharField(max_length=1000, blank=True, null=True)
    vp_participantes = models.CharField(max_length=250, blank=True, null=True)
    vp_personajes = models.CharField(max_length=250, blank=True, null=True)
    vp_areaconocimiento = models.CharField(max_length=50, blank=True, null=True)
    vp_asigmateria = models.CharField(max_length=50, blank=True, null=True)
    vp_niveleducativo = models.CharField(max_length=38, blank=True, null=True)
    vp_grado = models.CharField(max_length=40, blank=True, null=True)
    vp_ejetematico = models.CharField(max_length=100, blank=True, null=True)
    vp_tema = models.CharField(max_length=100, blank=True, null=True)
    vp_institproductora = models.CharField(max_length=300, blank=True, null=True)
    vp_idiomaoriginal = models.CharField(max_length=40, blank=True, null=True)
    vp_elenco = models.CharField(max_length=100, blank=True, null=True)
    vp_conductor = models.CharField(max_length=60, blank=True, null=True)
    vp_locutor = models.CharField(max_length=60, blank=True, null=True)
    vp_guionista = models.CharField(max_length=60, blank=True, null=True)
    vp_investigador = models.CharField(max_length=60, blank=True, null=True)
    vp_derechopatrimonial = models.CharField(max_length=60, blank=True, null=True)
    vp_fechacalificacion = models.DateTimeField(blank=True, null=True)
    vp_calificador = models.CharField(max_length=5, blank=True, null=True)
    vp_fecha_modificacion = models.DateTimeField(blank=True, null=True)
    vp_calificadormod = models.CharField(max_length=5, blank=True, null=True)
    vp_sistema = models.CharField(max_length=4, blank=True, null=True)
    vp_duracion = models.CharField(max_length=10, blank=True, null=True)
    vp_programa = models.CharField(max_length=300, blank=True, null=True)
    vp_subtitserie = models.TextField(blank=True, null=True)
    vp_orientacion = models.CharField(max_length=160, blank=True, null=True)
    vp_duracionin = models.CharField(max_length=165, blank=True, null=True)
    vp_duracionout = models.CharField(max_length=165, blank=True, null=True)
    vp_duracion1 = models.CharField(max_length=165, blank=True, null=True)
    tx = models.CharField(max_length=160, blank=True, null=True)
    vp_observaciones = models.CharField(max_length=1000, blank=True, null=True)
    vp_fork = models.CharField(max_length=300, blank=True, null=True)
    vp_realizador = models.CharField(max_length=600, blank=True, null=True)
    vp_musicao = models.CharField(max_length=600, blank=True, null=True)
    vp_musicai = models.CharField(max_length=600, blank=True, null=True)
    vp_cantante = models.CharField(max_length=600, blank=True, null=True)
    vp_disquera = models.CharField(max_length=600, blank=True, null=True)
    vp_libreriam = models.CharField(max_length=600, blank=True, null=True)
    vp_registro_obra = models.CharField(max_length=600, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'detalle_programas'


class FichaContenido(models.Model):
    id_segmento = models.IntegerField()
    id_pregunta = models.IntegerField()
    pregunta = models.CharField(max_length=134)
    fecha_alta = models.DateTimeField()
    status = models.CharField(max_length=1)
    tipo = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'ficha_contenido'


class FormatosCintas(models.Model):
    form_clave = models.IntegerField(primary_key=True)
    form_descripcion = models.CharField(max_length=25)
    form_duracion = models.CharField(max_length=10, blank=True, null=True)
    form_prefijo = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'formatos_cintas'


class HistoriaPrestamos(models.Model):
    hipr_clave = models.IntegerField(primary_key=True)
    usvi_clave = models.IntegerField()
    vide_clave = models.IntegerField()
    hisp_fechahora_registro = models.DateTimeField()
    hisp_fechahora_devolucion = models.DateTimeField(blank=True, null=True)
    dev_recibe = models.CharField(max_length=45, blank=True, null=True)
    dev_folio = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'historia_prestamos'


class IngresoMaterial(models.Model):
    folio_calificacion = models.CharField(max_length=15, blank=True, null=True)
    folio_videoteca = models.IntegerField(blank=True, null=True)
    fentrega_calificacon = models.CharField(max_length=15, blank=True, null=True)
    fingreso_videoteca = models.DateTimeField(blank=True, null=True)
    video_id = models.IntegerField()
    numero_produccion = models.IntegerField(blank=True, null=True)
    numero_presupuesto = models.IntegerField(blank=True, null=True)
    usua_entrega = models.CharField(max_length=45, blank=True, null=True)
    usua_videoteca = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'ingreso_material'


class Invrfid(models.Model):
    video_cbarras = models.CharField(primary_key=True, max_length=12)

    class Meta:
        managed = False
        db_table = 'invrfid'


class MaestroCintas(models.Model):
    video_id = models.IntegerField()
    video_cbarras = models.CharField(max_length=12)
    form_clave = models.IntegerField()
    video_idproduccion = models.IntegerField(blank=True, null=True)
    video_codificacion = models.CharField(max_length=20, blank=True, null=True)
    video_tipo = models.CharField(max_length=1, blank=True, null=True)
    video_fingreso = models.DateTimeField(blank=True, null=True)
    video_inventario = models.CharField(max_length=4, blank=True, null=True)
    video_estatus = models.CharField(max_length=20)
    video_rack = models.CharField(max_length=4, blank=True, null=True)
    video_nivel = models.CharField(max_length=4, blank=True, null=True)
    video_anoproduccion = models.IntegerField(blank=True, null=True)
    video_idproductor = models.IntegerField(blank=True, null=True)
    video_productor = models.CharField(max_length=55, blank=True, null=True)
    video_idcoordinador = models.IntegerField(blank=True, null=True)
    video_coordinador = models.CharField(max_length=60, blank=True, null=True)
    video_usmov = models.IntegerField(blank=True, null=True)
    video_fechamov = models.DateTimeField(blank=True, null=True)
    video_observaciones = models.CharField(max_length=238, blank=True, null=True)
    usua_clave = models.CharField(max_length=10, blank=True, null=True)
    video_fchcal = models.DateTimeField(blank=True, null=True)
    video_target = models.CharField(max_length=20, blank=True, null=True)
    id_tipo = models.IntegerField(blank=True, null=True)
    id_origen = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'maestro_cintas'


class NombreProgramas(models.Model):
    noproduccion = models.IntegerField()
    no_control = models.IntegerField()
    nomprog = models.CharField(max_length=10)
    durprog = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nombre_programas'


class OrdenTrabajo(models.Model):
    id_ot = models.IntegerField(primary_key=True)
    sinopsis = models.CharField(max_length=200)
    tiempo_in = models.CharField(max_length=11)
    tiempo_out = models.CharField(max_length=11)
    duracion = models.CharField(max_length=11)
    id_patrimonial = models.IntegerField(blank=True, null=True)
    palabras_clave = models.CharField(max_length=32)
    areaconocimiento = models.IntegerField(blank=True, null=True)
    niveleducativo = models.IntegerField(blank=True, null=True)
    asignatura = models.IntegerField(blank=True, null=True)
    id_eje = models.IntegerField(blank=True, null=True)
    tema = models.CharField(max_length=50)
    grado = models.IntegerField(blank=True, null=True)
    orientacion = models.IntegerField(blank=True, null=True)
    observaciones = models.CharField(max_length=100)
    idioma = models.IntegerField(blank=True, null=True)
    sistema = models.IntegerField(blank=True, null=True)
    presupuesto = models.CharField(max_length=12, blank=True, null=True)
    id_instproductora = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orden_trabajo'


class OrigenSerie(models.Model):
    id_origen = models.IntegerField()
    origen = models.CharField(max_length=35)

    class Meta:
        managed = False
        db_table = 'origen_serie'


class OtD(models.Model):
    id_ot = models.IntegerField()
    nombre = models.CharField(max_length=35)
    sinopsis = models.CharField(max_length=300)
    palabras_c = models.CharField(max_length=60)
    fecha = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ot_d'


class OtM(models.Model):
    id_ot = models.IntegerField(primary_key=True)
    asignatura = models.CharField(max_length=10, blank=True, null=True)
    participantes = models.CharField(max_length=70)
    nivel_e = models.CharField(max_length=25, blank=True, null=True)
    presupuesto_b = models.CharField(max_length=12, blank=True, null=True)
    area_c = models.CharField(max_length=18, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ot_m'


class Personas(models.Model):
    id_ot = models.IntegerField()
    id_personas = models.IntegerField()
    id_puesto = models.IntegerField()
    nombre = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'personas'


class PorIngresar(models.Model):
    video_cbarras = models.CharField(primary_key=True, max_length=12)
    ingresado = models.CharField(max_length=1)
    fch_captura = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'por_ingresar'


class Prestamos(models.Model):
    pres_folio = models.IntegerField(primary_key=True)
    usvi_clave = models.IntegerField()
    usua_clave = models.CharField(max_length=10)
    pres_fechahora = models.DateTimeField()
    pres_fecha_prestamo = models.DateTimeField()
    pres_fecha_devolucion = models.DateTimeField()
    pres_estatus = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'prestamos'


class Recupera(models.Model):
    video_clave = models.CharField(max_length=10)
    matricula = models.IntegerField()
    foliopres = models.IntegerField()
    fechapres = models.DateTimeField()
    fechadev = models.DateTimeField()
    cbarras = models.CharField(max_length=12)
    orden = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'recupera'


class RegistroCalificacion(models.Model):
    codigo_original = models.CharField(max_length=14, blank=True, null=True)
    codigo_barras = models.CharField(max_length=12)
    serie = models.CharField(max_length=120, blank=True, null=True)
    programa = models.CharField(max_length=150, blank=True, null=True)
    subtitulo_programa = models.CharField(max_length=100, blank=True, null=True)
    axo_produccion = models.CharField(max_length=10, blank=True, null=True)
    duracion = models.CharField(max_length=11, blank=True, null=True)
    id_productor = models.IntegerField(blank=True, null=True)
    productor = models.CharField(max_length=30, blank=True, null=True)
    id_coordinador = models.IntegerField(blank=True, null=True)
    coordinador = models.CharField(max_length=40, blank=True, null=True)
    sinopsis = models.CharField(max_length=1000, blank=True, null=True)
    participantes = models.CharField(max_length=200, blank=True, null=True)
    personajes = models.CharField(max_length=45, blank=True, null=True)
    area_de_conocimiento = models.CharField(max_length=35, blank=True, null=True)
    asignatura_materia = models.CharField(max_length=39, blank=True, null=True)
    nivel_educativo = models.CharField(max_length=12, blank=True, null=True)
    grado = models.CharField(max_length=17, blank=True, null=True)
    eje_tematico = models.CharField(max_length=168, blank=True, null=True)
    tema = models.CharField(max_length=187, blank=True, null=True)
    institucion_productora = models.CharField(max_length=200, blank=True, null=True)
    derecho_patrimonial = models.CharField(max_length=30, blank=True, null=True)
    idioma_original = models.CharField(max_length=8)
    elenco = models.CharField(max_length=100, blank=True, null=True)
    conductor = models.CharField(max_length=80, blank=True, null=True)
    locutor = models.CharField(max_length=80, blank=True, null=True)
    guionista = models.CharField(max_length=80, blank=True, null=True)
    investigador = models.CharField(max_length=90, blank=True, null=True)
    fecha_calificacion = models.DateTimeField()
    calificador = models.CharField(max_length=5, blank=True, null=True)
    fecha_modificacion = models.DateTimeField()
    calificador_modificacion = models.CharField(max_length=5, blank=True, null=True)
    sistema = models.CharField(max_length=4)
    codigo_orig1 = models.CharField(max_length=15, blank=True, null=True)
    codigo_submaster1 = models.CharField(max_length=12, blank=True, null=True)
    codigo_orig2 = models.CharField(max_length=14, blank=True, null=True)
    codigo_submaster2 = models.CharField(max_length=12, blank=True, null=True)
    codigo_orig3 = models.CharField(max_length=10, blank=True, null=True)
    codigo_submaster3 = models.CharField(max_length=12, blank=True, null=True)
    codigo_orig4 = models.CharField(max_length=15, blank=True, null=True)
    codigo_submaster4 = models.CharField(max_length=15, blank=True, null=True)
    codigo_orig5 = models.CharField(max_length=15, blank=True, null=True)
    codigo_submaster5 = models.CharField(max_length=15, blank=True, null=True)
    codigo_orig6 = models.CharField(max_length=15, blank=True, null=True)
    codigo_submaster6 = models.CharField(max_length=15, blank=True, null=True)
    subtitserie = models.CharField(max_length=100, blank=True, null=True)
    tiempoin = models.CharField(max_length=11, blank=True, null=True)
    tiempoout = models.CharField(max_length=11, blank=True, null=True)
    tiempodur = models.CharField(max_length=11, blank=True, null=True)
    orientacion = models.CharField(max_length=30, blank=True, null=True)
    observaciones = models.CharField(max_length=995, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'registro_calificacion'


class RegistroStock(models.Model):
    codificiacion = models.CharField(max_length=15, blank=True, null=True)
    codigo_barras = models.CharField(max_length=12)
    tipo_cinta = models.CharField(max_length=1)
    consecutivo = models.IntegerField()
    serie = models.CharField(max_length=107)
    subtitserie = models.CharField(max_length=35, blank=True, null=True)
    programa = models.CharField(max_length=150)
    subtitulo_programa = models.CharField(max_length=50, blank=True, null=True)
    axo_produccion = models.CharField(max_length=5, blank=True, null=True)
    tiempoin = models.CharField(max_length=15)
    tiempoinf = models.CharField(max_length=15, blank=True, null=True)
    tiempoout = models.CharField(max_length=15, blank=True, null=True)
    tiempooutf = models.CharField(max_length=11, blank=True, null=True)
    tiempodurf = models.CharField(max_length=15, blank=True, null=True)
    duracion = models.CharField(max_length=15)
    productor = models.CharField(max_length=40, blank=True, null=True)
    coordinador = models.CharField(max_length=40, blank=True, null=True)
    sinopsis = models.CharField(max_length=650, blank=True, null=True)
    participantes = models.CharField(max_length=130, blank=True, null=True)
    personajes = models.CharField(max_length=15, blank=True, null=True)
    institucion_productora = models.CharField(max_length=90, blank=True, null=True)
    derecho_patrimonial = models.CharField(max_length=5, blank=True, null=True)
    idioma_original = models.CharField(max_length=15)
    elenco = models.CharField(max_length=15, blank=True, null=True)
    conductor = models.CharField(max_length=23, blank=True, null=True)
    locutor = models.CharField(max_length=15, blank=True, null=True)
    guionista = models.CharField(max_length=15, blank=True, null=True)
    investigador = models.CharField(max_length=15, blank=True, null=True)
    fecha_calificacion = models.DateTimeField()
    calificador = models.CharField(max_length=5)
    fecha_modificacion = models.DateTimeField()
    calificador_modificacion = models.CharField(max_length=5, blank=True, null=True)
    sistema = models.CharField(max_length=4)
    observaciones = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'registro_stock'


class RegistroSubmaster(models.Model):
    codigo_original = models.CharField(max_length=14, blank=True, null=True)
    codigo_barras = models.CharField(max_length=15, blank=True, null=True)
    serie = models.CharField(max_length=120, blank=True, null=True)
    programa = models.CharField(max_length=140)
    subtitulo_programa = models.CharField(max_length=64, blank=True, null=True)
    axo_produccion = models.IntegerField(blank=True, null=True)
    duracion = models.CharField(max_length=8, blank=True, null=True)
    id_productor = models.IntegerField(blank=True, null=True)
    productor = models.CharField(max_length=32, blank=True, null=True)
    id_coordinador = models.IntegerField(blank=True, null=True)
    coordinador = models.CharField(max_length=40, blank=True, null=True)
    sinopsis = models.CharField(max_length=900, blank=True, null=True)
    participantes = models.CharField(max_length=200, blank=True, null=True)
    personajes = models.CharField(max_length=45, blank=True, null=True)
    area_de_conocimiento = models.CharField(max_length=40, blank=True, null=True)
    asignatura_materia = models.CharField(max_length=60, blank=True, null=True)
    nivel_educativo = models.CharField(max_length=15, blank=True, null=True)
    grado = models.CharField(max_length=20, blank=True, null=True)
    eje_tematico = models.CharField(max_length=160, blank=True, null=True)
    tema = models.CharField(max_length=200, blank=True, null=True)
    institucion_productora = models.CharField(max_length=200, blank=True, null=True)
    derecho_patrimonial = models.CharField(max_length=90, blank=True, null=True)
    idioma_original = models.CharField(max_length=30)
    elenco = models.CharField(max_length=100, blank=True, null=True)
    conductor = models.CharField(max_length=60, blank=True, null=True)
    locutor = models.CharField(max_length=59, blank=True, null=True)
    guionista = models.CharField(max_length=70, blank=True, null=True)
    investigador = models.CharField(max_length=69, blank=True, null=True)
    fecha_calificacion = models.DateTimeField()
    calificador = models.CharField(max_length=5, blank=True, null=True)
    fecha_modificacion = models.DateTimeField()
    calificador_modificacion = models.CharField(max_length=5)
    sistema = models.CharField(max_length=4)
    codigo_orig1 = models.CharField(max_length=16, blank=True, null=True)
    codigo_submaster1 = models.CharField(max_length=12, blank=True, null=True)
    codigo_orig2 = models.CharField(max_length=10, blank=True, null=True)
    codigo_submaster2 = models.CharField(max_length=12, blank=True, null=True)
    codigo_orig3 = models.CharField(max_length=10, blank=True, null=True)
    codigo_submaster3 = models.CharField(max_length=12, blank=True, null=True)
    codigo_orig4 = models.CharField(max_length=10, blank=True, null=True)
    codigo_submaster4 = models.CharField(max_length=12, blank=True, null=True)
    codigo_orig5 = models.CharField(max_length=10, blank=True, null=True)
    codigo_submaster5 = models.CharField(max_length=12, blank=True, null=True)
    codigo_orig6 = models.CharField(max_length=15, blank=True, null=True)
    codigo_submaster6 = models.CharField(max_length=15, blank=True, null=True)
    subtitserie = models.CharField(max_length=100, blank=True, null=True)
    tiempoin = models.CharField(max_length=11, blank=True, null=True)
    tiempoout = models.CharField(max_length=11, blank=True, null=True)
    tiempodur = models.CharField(max_length=11, blank=True, null=True)
    orientacion = models.CharField(max_length=30, blank=True, null=True)
    observaciones = models.CharField(max_length=900, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'registro_submaster'


class RelacionesVideos(models.Model):
    vide_clave = models.IntegerField()
    revi_clave = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'relaciones_videos'


class SolicitudMaterial(models.Model):
    noproduccion = models.IntegerField()
    no_control = models.IntegerField()
    observacionescintas = models.CharField(max_length=25, blank=True, null=True)
    cantidad = models.IntegerField()
    id_status = models.CharField(max_length=3)
    form_clave = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'solicitud_material'


class StockMatvirgen(models.Model):
    folio_cb = models.CharField(primary_key=True, max_length=12)
    codigobarras = models.CharField(max_length=15, blank=True, null=True)
    id_status = models.CharField(max_length=1)
    form_clave = models.IntegerField()
    no_reciclado = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'stock_matvirgen'


class Tbinventario(models.Model):
    cbarras = models.CharField(max_length=12)

    class Meta:
        managed = False
        db_table = 'tbinventario'


class TipoSerie(models.Model):
    id_tipo = models.IntegerField()
    tipo = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'tipo_serie'


class Usuarios(models.Model):
    usua_clave = models.CharField(max_length=15)
    usua_password = models.CharField(max_length=20, blank=True, null=True)
    usua_nombre = models.CharField(max_length=40)
    usua_tipo = models.CharField(max_length=1)
    usua_estatus = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'usuarios'


class UsuariosVid(models.Model):
    usvi_clave = models.CharField(max_length=45, blank=True, null=True)
    usvi_paterno = models.CharField(max_length=30)
    usvi_materno = models.CharField(max_length=30)
    usvi_nombre = models.CharField(max_length=30)
    usvi_maxvideos = models.IntegerField()
    usvi_vidpretados = models.IntegerField()
    usvi_diasprestamo = models.IntegerField()
    usvi_tipo = models.CharField(max_length=45, blank=True, null=True)
    matricula = models.IntegerField()
    area = models.CharField(max_length=40)
    activo = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuarios_vid'


class Videos(models.Model):
    vide_clave = models.IntegerField(primary_key=True)
    vide_codigo = models.CharField(max_length=12, blank=True, null=True)
    vide_videoteca = models.CharField(max_length=45, blank=True, null=True)
    vide_numero_cinta = models.CharField(max_length=14, blank=True, null=True)
    vide_tipo_video = models.CharField(max_length=4, blank=True, null=True)
    form_clave = models.IntegerField(blank=True, null=True)
    vide_consecutivo = models.IntegerField(blank=True, null=True)
    tivi_clave = models.CharField(max_length=45, blank=True, null=True)
    usvi_clave = models.IntegerField(blank=True, null=True)
    vide_fecha_ingreso = models.CharField(max_length=45, blank=True, null=True)
    vide_cinta_programa = models.CharField(max_length=45, blank=True, null=True)
    vide_cintas_totales = models.CharField(max_length=45, blank=True, null=True)
    vide_programas_totales = models.CharField(max_length=45, blank=True, null=True)
    vide_inventario = models.CharField(max_length=1)
    vide_estatus = models.CharField(max_length=1)
    usua_captura = models.CharField(max_length=10, blank=True, null=True)
    usua_modifica = models.CharField(max_length=10, blank=True, null=True)
    vide_fechahora_modificacion = models.DateTimeField(blank=True, null=True)
    marca = models.CharField(max_length=15, blank=True, null=True)
    vide_rack = models.CharField(max_length=45, blank=True, null=True)
    vide_nivel = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'videos'


class VideosPaso(models.Model):
    video_id = models.IntegerField()
    video_cbarras = models.CharField(max_length=12)
    video_rel_id = models.IntegerField()
    video_rel_cbarras = models.CharField(max_length=12)

    class Meta:
        managed = False
        db_table = 'videos_paso'


class VideosProgramas(models.Model):
    vide_clave = models.IntegerField(blank=True, null=True)
    vipr_indice = models.IntegerField()
    vipr_serie = models.CharField(max_length=310, blank=True, null=True)
    vipr_programa = models.CharField(max_length=320)
    vipr_productor = models.CharField(max_length=180, blank=True, null=True)
    vipr_leccion = models.CharField(max_length=50, blank=True, null=True)
    vipr_ano = models.CharField(max_length=45, blank=True, null=True)
    vipr_sinopsis = models.CharField(max_length=610, blank=True, null=True)
    vipr_palabras = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'videos_programas'


class VideosRelacionados(models.Model):
    video_id = models.CharField(max_length=12, blank=True, null=True)
    video_cbarras = models.CharField(max_length=12, blank=True, null=True)
    video_rel_id = models.CharField(max_length=12, blank=True, null=True)
    video_rel_cbarras = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'videos_relacionados'