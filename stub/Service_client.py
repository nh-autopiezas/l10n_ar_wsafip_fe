##################################################
# file: Service_client.py
# 
# client stubs generated by "ZSI.generate.wsdl2python.WriteServiceModule"
#     /usr/bin/wsdl2py -b service.wsdl
# 
##################################################

from Service_types import *
import urlparse, types
from ZSI.TCcompound import ComplexType, Struct
from ZSI import client
from ZSI.schema import GED, GTD
import ZSI
from ZSI.generate.pyclass import pyclass_type

# Locator
class ServiceLocator:
    ServiceSoap_address = "https://servicios1.afip.gov.ar/wsfev1/service.asmx"
    def getServiceSoapAddress(self):
        return ServiceLocator.ServiceSoap_address
    def getServiceSoap(self, url=None, **kw):
        return ServiceSoapSOAP(url or ServiceLocator.ServiceSoap_address, **kw)

# Methods
class ServiceSoapSOAP:
    def __init__(self, url, **kw):
        kw.setdefault("readerclass", None)
        kw.setdefault("writerclass", None)
        # no resource properties
        self.binding = client.Binding(url=url, **kw)
        # no ws-addressing

    # op: FECAESolicitar
    def FECAESolicitar(self, request, **kw):
        if isinstance(request, FECAESolicitarSoapIn) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="http://ar.gov.afip.dif.FEV1/FECAESolicitar", **kw)
        # no output wsaction
        response = self.binding.Receive(FECAESolicitarSoapOut.typecode)
        return response

    # op: FECompTotXRequest
    def FECompTotXRequest(self, request, **kw):
        if isinstance(request, FECompTotXRequestSoapIn) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="http://ar.gov.afip.dif.FEV1/FECompTotXRequest", **kw)
        # no output wsaction
        response = self.binding.Receive(FECompTotXRequestSoapOut.typecode)
        return response

    # op: FEDummy
    def FEDummy(self, request, **kw):
        if isinstance(request, FEDummySoapIn) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="http://ar.gov.afip.dif.FEV1/FEDummy", **kw)
        # no output wsaction
        response = self.binding.Receive(FEDummySoapOut.typecode)
        return response

    # op: FECompUltimoAutorizado
    def FECompUltimoAutorizado(self, request, **kw):
        if isinstance(request, FECompUltimoAutorizadoSoapIn) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="http://ar.gov.afip.dif.FEV1/FECompUltimoAutorizado", **kw)
        # no output wsaction
        response = self.binding.Receive(FECompUltimoAutorizadoSoapOut.typecode)
        return response

    # op: FECompConsultar
    def FECompConsultar(self, request, **kw):
        if isinstance(request, FECompConsultarSoapIn) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="http://ar.gov.afip.dif.FEV1/FECompConsultar", **kw)
        # no output wsaction
        response = self.binding.Receive(FECompConsultarSoapOut.typecode)
        return response

    # op: FECAEARegInformativo
    def FECAEARegInformativo(self, request, **kw):
        if isinstance(request, FECAEARegInformativoSoapIn) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="http://ar.gov.afip.dif.FEV1/FECAEARegInformativo", **kw)
        # no output wsaction
        response = self.binding.Receive(FECAEARegInformativoSoapOut.typecode)
        return response

    # op: FECAEASolicitar
    def FECAEASolicitar(self, request, **kw):
        if isinstance(request, FECAEASolicitarSoapIn) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="http://ar.gov.afip.dif.FEV1/FECAEASolicitar", **kw)
        # no output wsaction
        response = self.binding.Receive(FECAEASolicitarSoapOut.typecode)
        return response

    # op: FECAEASinMovimientoConsultar
    def FECAEASinMovimientoConsultar(self, request, **kw):
        if isinstance(request, FECAEASinMovimientoConsultarSoapIn) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="http://ar.gov.afip.dif.FEV1/FECAEASinMovimientoConsultar", **kw)
        # no output wsaction
        response = self.binding.Receive(FECAEASinMovimientoConsultarSoapOut.typecode)
        return response

    # op: FECAEASinMovimientoInformar
    def FECAEASinMovimientoInformar(self, request, **kw):
        if isinstance(request, FECAEASinMovimientoInformarSoapIn) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="http://ar.gov.afip.dif.FEV1/FECAEASinMovimientoInformar", **kw)
        # no output wsaction
        response = self.binding.Receive(FECAEASinMovimientoInformarSoapOut.typecode)
        return response

    # op: FECAEAConsultar
    def FECAEAConsultar(self, request, **kw):
        if isinstance(request, FECAEAConsultarSoapIn) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="http://ar.gov.afip.dif.FEV1/FECAEAConsultar", **kw)
        # no output wsaction
        response = self.binding.Receive(FECAEAConsultarSoapOut.typecode)
        return response

    # op: FEParamGetCotizacion
    def FEParamGetCotizacion(self, request, **kw):
        if isinstance(request, FEParamGetCotizacionSoapIn) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="http://ar.gov.afip.dif.FEV1/FEParamGetCotizacion", **kw)
        # no output wsaction
        response = self.binding.Receive(FEParamGetCotizacionSoapOut.typecode)
        return response

    # op: FEParamGetTiposTributos
    def FEParamGetTiposTributos(self, request, **kw):
        if isinstance(request, FEParamGetTiposTributosSoapIn) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="http://ar.gov.afip.dif.FEV1/FEParamGetTiposTributos", **kw)
        # no output wsaction
        response = self.binding.Receive(FEParamGetTiposTributosSoapOut.typecode)
        return response

    # op: FEParamGetTiposMonedas
    def FEParamGetTiposMonedas(self, request, **kw):
        if isinstance(request, FEParamGetTiposMonedasSoapIn) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="http://ar.gov.afip.dif.FEV1/FEParamGetTiposMonedas", **kw)
        # no output wsaction
        response = self.binding.Receive(FEParamGetTiposMonedasSoapOut.typecode)
        return response

    # op: FEParamGetTiposIva
    def FEParamGetTiposIva(self, request, **kw):
        if isinstance(request, FEParamGetTiposIvaSoapIn) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="http://ar.gov.afip.dif.FEV1/FEParamGetTiposIva", **kw)
        # no output wsaction
        response = self.binding.Receive(FEParamGetTiposIvaSoapOut.typecode)
        return response

    # op: FEParamGetTiposOpcional
    def FEParamGetTiposOpcional(self, request, **kw):
        if isinstance(request, FEParamGetTiposOpcionalSoapIn) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="http://ar.gov.afip.dif.FEV1/FEParamGetTiposOpcional", **kw)
        # no output wsaction
        response = self.binding.Receive(FEParamGetTiposOpcionalSoapOut.typecode)
        return response

    # op: FEParamGetTiposConcepto
    def FEParamGetTiposConcepto(self, request, **kw):
        if isinstance(request, FEParamGetTiposConceptoSoapIn) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="http://ar.gov.afip.dif.FEV1/FEParamGetTiposConcepto", **kw)
        # no output wsaction
        response = self.binding.Receive(FEParamGetTiposConceptoSoapOut.typecode)
        return response

    # op: FEParamGetPtosVenta
    def FEParamGetPtosVenta(self, request, **kw):
        if isinstance(request, FEParamGetPtosVentaSoapIn) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="http://ar.gov.afip.dif.FEV1/FEParamGetPtosVenta", **kw)
        # no output wsaction
        response = self.binding.Receive(FEParamGetPtosVentaSoapOut.typecode)
        return response

    # op: FEParamGetTiposCbte
    def FEParamGetTiposCbte(self, request, **kw):
        if isinstance(request, FEParamGetTiposCbteSoapIn) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="http://ar.gov.afip.dif.FEV1/FEParamGetTiposCbte", **kw)
        # no output wsaction
        response = self.binding.Receive(FEParamGetTiposCbteSoapOut.typecode)
        return response

    # op: FEParamGetTiposDoc
    def FEParamGetTiposDoc(self, request, **kw):
        if isinstance(request, FEParamGetTiposDocSoapIn) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="http://ar.gov.afip.dif.FEV1/FEParamGetTiposDoc", **kw)
        # no output wsaction
        response = self.binding.Receive(FEParamGetTiposDocSoapOut.typecode)
        return response

FECAESolicitarSoapIn = GED("http://ar.gov.afip.dif.FEV1/", "FECAESolicitar").pyclass

FECAESolicitarSoapOut = GED("http://ar.gov.afip.dif.FEV1/", "FECAESolicitarResponse").pyclass

FECompTotXRequestSoapIn = GED("http://ar.gov.afip.dif.FEV1/", "FECompTotXRequest").pyclass

FECompTotXRequestSoapOut = GED("http://ar.gov.afip.dif.FEV1/", "FECompTotXRequestResponse").pyclass

FEDummySoapIn = GED("http://ar.gov.afip.dif.FEV1/", "FEDummy").pyclass

FEDummySoapOut = GED("http://ar.gov.afip.dif.FEV1/", "FEDummyResponse").pyclass

FECompUltimoAutorizadoSoapIn = GED("http://ar.gov.afip.dif.FEV1/", "FECompUltimoAutorizado").pyclass

FECompUltimoAutorizadoSoapOut = GED("http://ar.gov.afip.dif.FEV1/", "FECompUltimoAutorizadoResponse").pyclass

FECompConsultarSoapIn = GED("http://ar.gov.afip.dif.FEV1/", "FECompConsultar").pyclass

FECompConsultarSoapOut = GED("http://ar.gov.afip.dif.FEV1/", "FECompConsultarResponse").pyclass

FECAEARegInformativoSoapIn = GED("http://ar.gov.afip.dif.FEV1/", "FECAEARegInformativo").pyclass

FECAEARegInformativoSoapOut = GED("http://ar.gov.afip.dif.FEV1/", "FECAEARegInformativoResponse").pyclass

FECAEASolicitarSoapIn = GED("http://ar.gov.afip.dif.FEV1/", "FECAEASolicitar").pyclass

FECAEASolicitarSoapOut = GED("http://ar.gov.afip.dif.FEV1/", "FECAEASolicitarResponse").pyclass

FECAEASinMovimientoConsultarSoapIn = GED("http://ar.gov.afip.dif.FEV1/", "FECAEASinMovimientoConsultar").pyclass

FECAEASinMovimientoConsultarSoapOut = GED("http://ar.gov.afip.dif.FEV1/", "FECAEASinMovimientoConsultarResponse").pyclass

FECAEASinMovimientoInformarSoapIn = GED("http://ar.gov.afip.dif.FEV1/", "FECAEASinMovimientoInformar").pyclass

FECAEASinMovimientoInformarSoapOut = GED("http://ar.gov.afip.dif.FEV1/", "FECAEASinMovimientoInformarResponse").pyclass

FECAEAConsultarSoapIn = GED("http://ar.gov.afip.dif.FEV1/", "FECAEAConsultar").pyclass

FECAEAConsultarSoapOut = GED("http://ar.gov.afip.dif.FEV1/", "FECAEAConsultarResponse").pyclass

FEParamGetCotizacionSoapIn = GED("http://ar.gov.afip.dif.FEV1/", "FEParamGetCotizacion").pyclass

FEParamGetCotizacionSoapOut = GED("http://ar.gov.afip.dif.FEV1/", "FEParamGetCotizacionResponse").pyclass

FEParamGetTiposTributosSoapIn = GED("http://ar.gov.afip.dif.FEV1/", "FEParamGetTiposTributos").pyclass

FEParamGetTiposTributosSoapOut = GED("http://ar.gov.afip.dif.FEV1/", "FEParamGetTiposTributosResponse").pyclass

FEParamGetTiposMonedasSoapIn = GED("http://ar.gov.afip.dif.FEV1/", "FEParamGetTiposMonedas").pyclass

FEParamGetTiposMonedasSoapOut = GED("http://ar.gov.afip.dif.FEV1/", "FEParamGetTiposMonedasResponse").pyclass

FEParamGetTiposIvaSoapIn = GED("http://ar.gov.afip.dif.FEV1/", "FEParamGetTiposIva").pyclass

FEParamGetTiposIvaSoapOut = GED("http://ar.gov.afip.dif.FEV1/", "FEParamGetTiposIvaResponse").pyclass

FEParamGetTiposOpcionalSoapIn = GED("http://ar.gov.afip.dif.FEV1/", "FEParamGetTiposOpcional").pyclass

FEParamGetTiposOpcionalSoapOut = GED("http://ar.gov.afip.dif.FEV1/", "FEParamGetTiposOpcionalResponse").pyclass

FEParamGetTiposConceptoSoapIn = GED("http://ar.gov.afip.dif.FEV1/", "FEParamGetTiposConcepto").pyclass

FEParamGetTiposConceptoSoapOut = GED("http://ar.gov.afip.dif.FEV1/", "FEParamGetTiposConceptoResponse").pyclass

FEParamGetPtosVentaSoapIn = GED("http://ar.gov.afip.dif.FEV1/", "FEParamGetPtosVenta").pyclass

FEParamGetPtosVentaSoapOut = GED("http://ar.gov.afip.dif.FEV1/", "FEParamGetPtosVentaResponse").pyclass

FEParamGetTiposCbteSoapIn = GED("http://ar.gov.afip.dif.FEV1/", "FEParamGetTiposCbte").pyclass

FEParamGetTiposCbteSoapOut = GED("http://ar.gov.afip.dif.FEV1/", "FEParamGetTiposCbteResponse").pyclass

FEParamGetTiposDocSoapIn = GED("http://ar.gov.afip.dif.FEV1/", "FEParamGetTiposDoc").pyclass

FEParamGetTiposDocSoapOut = GED("http://ar.gov.afip.dif.FEV1/", "FEParamGetTiposDocResponse").pyclass
