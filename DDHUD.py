# coding: utf8
###############################################################################
# Name:
#   DDHUD.py
#
# Author:
#   wangdonghao
#
# Usage:
#   createNode DDHUD;
#   createNode DDHUDBorder;
###############################################################################
import maya.api.OpenMaya as om
import maya.api.OpenMayaRender as omr
import maya.api.OpenMayaUI as omui

import maya.cmds as cmds


def maya_useNewAPI():
    """
    The presence of this function tells Maya that the plugin produces, and
    expects to be passed, objects created using the Maya Python API 2.0.
    """
    pass


class DDHUDBorderLocator(omui.MPxLocatorNode):
    """
    """
    NAME = 'DDHUDBorder'
    TYPE_ID = om.MTypeId(0x0011A887)
    DRAW_DB_CLASSIFICATION = 'drawdb/geometry/DDHUDBorder'
    DRAW_REGISTRANT_ID = 'DDHUDBorderNode'

    def __init__(self):
        """
        """
        super(DDHUDBorderLocator, self).__init__()

    def excludeAsLocator(self):
        """
        """
        return False

    @classmethod
    def creator(cls):
        """
        """
        return DDHUDBorderLocator()

    @classmethod
    def initialize(cls):
        #  相机
        cam_attr = om.MFnTypedAttribute()
        stringData = om.MFnStringData()
        obj = stringData.create("")
        camera_name = cam_attr.create("camera", "cam", om.MFnData.kString, obj)
        cam_attr.writable = True
        cam_attr.storable = True
        cam_attr.keyable = False
        DDHUDBorderLocator.addAttribute(camera_name)
        # 上遮罩高
        attr = om.MFnNumericAttribute()
        border_h = attr.create("topBorderHeight", "tbh", om.MFnNumericData.kFloat, 0.05)
        attr.writable = True
        attr.storable = True
        attr.keyable = True
        attr.setMin(-1)
        attr.setMax(1)
        DDHUDBorderLocator.addAttribute(border_h)
        # 上遮罩颜色
        attr = om.MFnNumericAttribute()
        border_color = attr.createColor("topBorderColor", "tbc")
        attr.default = (0.0, 0.0, 0.0)
        attr.writable = True
        attr.storable = True
        attr.keyable = True
        DDHUDBorderLocator.addAttribute(border_color)
        # 上遮罩透明度
        attr = om.MFnNumericAttribute()
        border_alpha = attr.create("topBorderAlpha", "tba", om.MFnNumericData.kFloat, 1.0)
        attr.writable = True
        attr.storable = True
        attr.keyable = True
        attr.setMin(0.0)
        attr.setMax(1.0)
        DDHUDBorderLocator.addAttribute(border_alpha)

        # 下遮罩高
        attr = om.MFnNumericAttribute()
        bborder_h = attr.create("bottomBorderHeight", "bbh", om.MFnNumericData.kFloat, 0.05)
        attr.writable = True
        attr.storable = True
        attr.keyable = True
        attr.setMin(-1)
        attr.setMax(1)
        DDHUDBorderLocator.addAttribute(bborder_h)
        # 下遮罩颜色
        attr = om.MFnNumericAttribute()
        bborder_color = attr.createColor("bottomBorderColor", "bbc")
        attr.default = (0.0, 0.0, 0.0)
        attr.writable = True
        attr.storable = True
        attr.keyable = True
        DDHUDBorderLocator.addAttribute(bborder_color)
        # 下遮罩透明度
        attr = om.MFnNumericAttribute()
        bborder_alpha = attr.create("bottomBorderAlpha", "bba", om.MFnNumericData.kFloat, 1.0)
        attr.writable = True
        attr.storable = True
        attr.keyable = True
        attr.setMin(0.0)
        attr.setMax(1.0)
        DDHUDBorderLocator.addAttribute(bborder_alpha)


class DDHUDLocator(omui.MPxLocatorNode):
    """
    """
    NAME = 'DDHUD'
    TYPE_ID = om.MTypeId(0x0011A889)
    DRAW_DB_CLASSIFICATION = 'drawdb/geometry/DDHUD'
    DRAW_REGISTRANT_ID = 'DDHUDNode'
    # 文字， 位置， 颜色， 大小
    # ATTRS = ["text", "t", "X", "x", 'Y', 'y', 'fontScale', 'fs', 'fontColor', 'fc', 'fontAlpha', 'fa',
    #          'border', 'b', 'borderWidth', 'bw', 'borderHeight', 'bh', 'borderColor', 'bc', 'borderAlpha', 'ba']

    def __init__(self):
        """
        """
        super(DDHUDLocator, self).__init__()

    def excludeAsLocator(self):
        """
        """
        return False

    @classmethod
    def creator(cls):
        """
        """
        return DDHUDLocator()

    @classmethod
    def initialize(cls):
        """
        """
        # 添加属性
        #  相机
        cam_attr = om.MFnTypedAttribute()
        stringData = om.MFnStringData()
        obj = stringData.create("")
        camera_name = cam_attr.create("camera", "cam", om.MFnData.kString, obj)
        cam_attr.writable = True
        cam_attr.storable = True
        cam_attr.keyable = False
        DDHUDLocator.addAttribute(camera_name)
        #  文字
        text_attr = om.MFnTypedAttribute()
        stringData = om.MFnStringData()
        obj = stringData.create("text")
        text = text_attr.create('text', 't', om.MFnData.kString, obj)
        text_attr.writable = True
        text_attr.storable = True
        text_attr.keyable = True
        DDHUDLocator.addAttribute(text)
        # 文字位置x
        attr = om.MFnNumericAttribute()
        x = attr.create("X", "x", om.MFnNumericData.kFloat, 0.5)
        attr.writable = True
        attr.storable = True
        attr.keyable = True
        attr.setMin(0.0)
        attr.setMax(1.0)
        DDHUDLocator.addAttribute(x)
        # 文字位置y
        attr = om.MFnNumericAttribute()
        y = attr.create("Y", "y", om.MFnNumericData.kFloat, 0.5)
        attr.writable = True
        attr.storable = True
        attr.keyable = True
        attr.setMin(0.0)
        attr.setMax(1.0)
        DDHUDLocator.addAttribute(y)
        # 字体名称
        t_attr = om.MFnTypedAttribute()
        stringData = om.MFnStringData()
        obj = stringData.create("Consolas")
        font_name = t_attr.create("fontName", "fn", om.MFnData.kString, obj)
        t_attr.writable = True
        t_attr.storable = True
        t_attr.keyable = True
        DDHUDLocator.addAttribute(font_name)
        # 文字大小
        attr = om.MFnNumericAttribute()
        font_scale = attr.create("fontScale", "fs", om.MFnNumericData.kFloat, 1.0)
        attr.writable = True
        attr.storable = True
        attr.keyable = True
        attr.setMin(0.1)
        attr.setMax(2.0)
        DDHUDLocator.addAttribute(font_scale)
        # 文字颜色
        attr = om.MFnNumericAttribute()
        font_color = attr.createColor("fontColor", "fc")
        attr.default = (1.0, 1.0, 1.0)
        attr.writable = True
        attr.storable = True
        attr.keyable = True
        DDHUDLocator.addAttribute(font_color)
        # 文字透明度
        attr = om.MFnNumericAttribute()
        font_alpha = attr.create("fontAlpha", "fa", om.MFnNumericData.kFloat, 1.0)
        attr.writable = True
        attr.storable = True
        attr.keyable = True
        attr.setMin(0.0)
        attr.setMax(1.0)
        DDHUDLocator.addAttribute(font_alpha)
        # 是否有遮罩
        attr = om.MFnNumericAttribute()
        border = attr.create("border", "b", om.MFnNumericData.kBoolean, True)
        attr.writable = True
        attr.storable = True
        attr.keyable = True
        DDHUDLocator.addAttribute(border)
        # 遮罩宽
        attr = om.MFnNumericAttribute()
        border_w = attr.create("borderWidth", "bw", om.MFnNumericData.kFloat, 2.0)
        attr.writable = True
        attr.storable = True
        attr.keyable = True
        attr.setMin(0.0)
        attr.setMax(100.0)
        DDHUDLocator.addAttribute(border_w)
        # 遮罩高
        attr = om.MFnNumericAttribute()
        border_h = attr.create("borderHeight", "bh", om.MFnNumericData.kFloat, 1.0)
        attr.writable = True
        attr.storable = True
        attr.keyable = True
        attr.setMin(0.0)
        attr.setMax(2.0)
        DDHUDLocator.addAttribute(border_h)
        # 遮罩颜色
        attr = om.MFnNumericAttribute()
        border_color = attr.createColor("borderColor", "bc")
        attr.default = (0.0, 0.0, 0.0)
        attr.writable = True
        attr.storable = True
        attr.keyable = True
        DDHUDLocator.addAttribute(border_color)
        # 遮罩透明度
        attr = om.MFnNumericAttribute()
        border_alpha = attr.create("borderAlpha", "ba", om.MFnNumericData.kFloat, 1.0)
        attr.writable = True
        attr.storable = True
        attr.keyable = True
        attr.setMin(0.0)
        attr.setMax(1.0)
        DDHUDLocator.addAttribute(border_alpha)
    
    
class DDHUDData(om.MUserData):
    """
    """

    def __init__(self):
        """
        """
        super(DDHUDData, self).__init__(False)


class DDHUDBorderData(om.MUserData):
    def __init__(self):
        """
        """
        super(DDHUDBorderData, self).__init__(False)


class DDHUDBorderDrawOverride(omr.MPxDrawOverride):
    """
    """
    NAME = "DDhud_border_draw_override"

    def __init__(self, obj):
        """
        """
        super(DDHUDBorderDrawOverride, self).__init__(obj, DDHUDBorderDrawOverride.draw)

    def supporteDDrawAPIs(self):
        """
        """
        return (omr.MRenderer.kAllDevices)

    def isBounded(self, obj_path, camera_path):
        """
        """
        return False

    def boundingBox(self, obj_path, camera_path):
        """
        """
        return om.MBoundingBox()

    def prepareForDraw(self, obj_path, camera_path, frame_context, old_data):
        """
        """
        data = old_data
        if not isinstance(data, DDHUDBorderData):
            data = DDHUDBorderData()

        fnDagNode = om.MFnDagNode(obj_path)
        data.camera_name = fnDagNode.findPlug("camera", False).asString()
        data.top_border_size = fnDagNode.findPlug("topBorderHeight", False).asFloat()
        r = fnDagNode.findPlug("topBorderColorR", False).asFloat()
        g = fnDagNode.findPlug("topBorderColorG", False).asFloat()
        b = fnDagNode.findPlug("topBorderColorB", False).asFloat()
        a = fnDagNode.findPlug("topBorderAlpha", False).asFloat()
        data.top_border_color = om.MColor((r, g, b, a))

        data.bottom_border_size = fnDagNode.findPlug("bottomBorderHeight", False).asFloat()
        r = fnDagNode.findPlug("bottomBorderColorR", False).asFloat()
        g = fnDagNode.findPlug("bottomBorderColorG", False).asFloat()
        b = fnDagNode.findPlug("bottomBorderColorB", False).asFloat()
        a = fnDagNode.findPlug("bottomBorderAlpha", False).asFloat()
        data.bottom_border_color = om.MColor((r, g, b, a))
        return data

    def hasUIDrawables(self):
        """
        """
        return True

    def addUIDrawables(self, obj_path, draw_manager, frame_context, data):
        """
        """
        if not isinstance(data, DDHUDBorderData):
            return

        camera_path = frame_context.getCurrentCameraPath()
        camera = om.MFnCamera(camera_path)

        if data.camera_name and camera_exists(data.camera_name) and not is_camera_match(camera_path,
                                                                                                  data.camera_name):
            return

        mask_width, mask_height = get_mask_size(camera, frame_context)
        vp_x, vp_y, vp_width, vp_height = frame_context.getViewportDimensions()
        vp_half_height = 0.5 * vp_height

        mask_half_height = 0.5 * mask_height
        mask_bottom_y = vp_half_height - mask_half_height
        mask_top_y = vp_half_height + mask_half_height

        top_border_height = int(mask_top_y - mask_height * data.top_border_size)
        top_background_size = (int(vp_width), vp_height - top_border_height)

        bottom_border_height = int(mask_height * data.bottom_border_size + mask_bottom_y)
        bottom_background_size = (int(vp_width), bottom_border_height)

        draw_manager.beginDrawable()

        draw_border(draw_manager, om.MPoint(0, top_border_height), top_background_size, data.top_border_color)
        draw_border(draw_manager, om.MPoint(0, 0), bottom_background_size, data.bottom_border_color)

    @staticmethod
    def creator(obj):
        """
        """
        return DDHUDBorderDrawOverride(obj)

    @staticmethod
    def draw(context, data):
        """
        """
        return


class DDHUDDrawOverride(omr.MPxDrawOverride):
    """
    """
    NAME = "DDhud_draw_override"

    def __init__(self, obj):
        """
        """
        super(DDHUDDrawOverride, self).__init__(obj, DDHUDDrawOverride.draw)

    def supporteDDrawAPIs(self):
        """
        """
        return (omr.MRenderer.kAllDevices)

    def isBounded(self, obj_path, camera_path):
        """
        """
        return False

    def boundingBox(self, obj_path, camera_path):
        """
        """
        return om.MBoundingBox()

    def prepareForDraw(self, obj_path, camera_path, frame_context, old_data):
        """
        """
        data = old_data
        if not isinstance(data, DDHUDData):
            data = DDHUDData()
        fnDagNode = om.MFnDagNode(obj_path)
        # 需要先获取数据
        data.camera_name = fnDagNode.findPlug("camera", False).asString()
        data.text = fnDagNode.findPlug("text", False).asString()
        data.font_name = fnDagNode.findPlug("fontName", False).asString()
        data.x = fnDagNode.findPlug("X", False).asFloat()
        data.y = fnDagNode.findPlug("Y", False).asFloat()
        r = fnDagNode.findPlug("fontColorR", False).asFloat()
        g = fnDagNode.findPlug("fontColorG", False).asFloat()
        b = fnDagNode.findPlug("fontColorB", False).asFloat()
        a = fnDagNode.findPlug("fontAlpha", False).asFloat()
        data.font_color = om.MColor((r, g, b, a))
        data.font_scale = fnDagNode.findPlug("fontScale", False).asFloat()
        data.border = fnDagNode.findPlug("border", False).asBool()
        r = fnDagNode.findPlug("borderColorR", False).asFloat()
        g = fnDagNode.findPlug("borderColorG", False).asFloat()
        b = fnDagNode.findPlug("borderColorB", False).asFloat()
        a = fnDagNode.findPlug("borderAlpha", False).asFloat()
        data.border_color = om.MColor((r, g, b, a))
        data.border_w = fnDagNode.findPlug("borderWidth", False).asFloat()
        data.border_h = fnDagNode.findPlug("borderHeight", False).asFloat()
        return data

    def hasUIDrawables(self):
        """
        """
        return True

    def addUIDrawables(self, obj_path, draw_manager, frame_context, data):
        """
        """
        if not isinstance(data, DDHUDData):
            return

        camera_path = frame_context.getCurrentCameraPath()
        camera = om.MFnCamera(camera_path)

        if data.camera_name and camera_exists(data.camera_name) and not is_camera_match(camera_path,
                                                                                                  data.camera_name):
            return
        mask_width, mask_height = get_mask_size(camera, frame_context)
        vp_x, vp_y, vp_width, vp_height = frame_context.getViewportDimensions()
        vp_half_width = 0.5 * vp_width
        vp_half_height = 0.5 * vp_height

        mask_half_width = 0.5 * mask_width
        mask_x = vp_half_width - mask_half_width

        mask_half_height = 0.5 * mask_height
        mask_top_y = vp_half_height + mask_half_height

        border_height = int(0.05 * mask_height * data.border_h)
        background_size = (int(data.border_w*border_height), int(data.border_h*border_height))

        draw_manager.beginDrawable()
        draw_manager.setFontName(data.font_name)
        draw_manager.setFontSize(int((border_height - border_height * 0.15) * data.font_scale))
        draw_manager.setColor(data.font_color)
        new_x = data.x * mask_width + mask_x
        new_y = -data.y * mask_height + mask_top_y
        if data.border:
            draw_border(draw_manager, om.MPoint(new_x, new_y), background_size,
                             data.border_color)
        draw_text(draw_manager, om.MPoint(new_x, new_y), data.text, omr.MUIDrawManager.kLeft, background_size)

    @staticmethod
    def creator(obj):
        """
        """
        return DDHUDDrawOverride(obj)

    @staticmethod
    def draw(context, data):
        """
        """
        return


def get_mask_size(camera, frame_context):

    camera_aspect_ratio = camera.aspectRatio()
    device_aspect_ratio = cmds.getAttr("defaultResolution.deviceAspectRatio")

    vp_x, vp_y, vp_width, vp_height = frame_context.getViewportDimensions()
    vp_aspect_ratio = vp_width / float(vp_height)

    scale = 1.0

    if camera.filmFit == om.MFnCamera.kHorizontalFilmFit:
        mask_width = vp_width / camera.overscan
        mask_height = mask_width / device_aspect_ratio
    elif camera.filmFit == om.MFnCamera.kVerticalFilmFit:
        mask_height = vp_height / camera.overscan
        mask_width = mask_height * device_aspect_ratio
    elif camera.filmFit == om.MFnCamera.kFillFilmFit:
        if vp_aspect_ratio < camera_aspect_ratio:
            if camera_aspect_ratio < device_aspect_ratio:
                scale = camera_aspect_ratio / vp_aspect_ratio
            else:
                scale = device_aspect_ratio / vp_aspect_ratio
        elif camera_aspect_ratio > device_aspect_ratio:
            scale = device_aspect_ratio / camera_aspect_ratio

        mask_width = vp_width / camera.overscan * scale
        mask_height = mask_width / device_aspect_ratio

    elif camera.filmFit == om.MFnCamera.kOverscanFilmFit:
        if vp_aspect_ratio < camera_aspect_ratio:
            if camera_aspect_ratio < device_aspect_ratio:
                scale = camera_aspect_ratio / vp_aspect_ratio
            else:
                scale = device_aspect_ratio / vp_aspect_ratio
        elif camera_aspect_ratio > device_aspect_ratio:
            scale = device_aspect_ratio / camera_aspect_ratio

        mask_height = vp_height / camera.overscan / scale
        mask_width = mask_height * device_aspect_ratio
    else:
        om.MGlobal.displayError("Unknown Film Fit value")
        return
    return mask_width, mask_height


def draw_border(draw_manager, position, background_size, color):
    draw_manager.text2d(position, " ", alignment=omr.MUIDrawManager.kLeft, backgroundSize=background_size,
                        backgroundColor=color)


def draw_text(draw_manager, position, text, alignment, background_size):
    if len(text) > 0:
        draw_manager.text2d(position, text, alignment=alignment, backgroundSize=background_size,
                            backgroundColor=om.MColor((0.0, 0.0, 0.0, 0.0)))
   
   
def camera_exists(name):
    return name in cmds.listCameras()


def is_camera_match(camera_path, name):
    """
    """
    path_name = camera_path.fullPathName()
    split_path_name = path_name.split('|')
    if len(split_path_name) >= 1:
        if split_path_name[-1] == name:
            return True
    if len(split_path_name) >= 2:
        if split_path_name[-2] == name:
            return True

    return False


def initializePlugin(obj):
    """
    """
    pluginFn = om.MFnPlugin(obj, "wangdonghao", "1.0.0", "Any")

    try:
        pluginFn.registerNode(DDHUDLocator.NAME,
                              DDHUDLocator.TYPE_ID,
                              DDHUDLocator.creator,
                              DDHUDLocator.initialize,
                              om.MPxNode.kLocatorNode,
                              DDHUDLocator.DRAW_DB_CLASSIFICATION)
        pluginFn.registerNode(DDHUDBorderLocator.NAME,
                              DDHUDBorderLocator.TYPE_ID,
                              DDHUDBorderLocator.creator,
                              DDHUDBorderLocator.initialize,
                              om.MPxNode.kLocatorNode,
                              DDHUDBorderLocator.DRAW_DB_CLASSIFICATION)
    except:
        om.MGlobal.displayError("Failed to register node: {0}".format(DDHUDLocator.NAME))

    try:
        omr.MDrawRegistry.registerDrawOverrideCreator(DDHUDLocator.DRAW_DB_CLASSIFICATION,
                                                      DDHUDLocator.DRAW_REGISTRANT_ID,
                                                      DDHUDDrawOverride.creator)
        omr.MDrawRegistry.registerDrawOverrideCreator(DDHUDBorderLocator.DRAW_DB_CLASSIFICATION,
                                                      DDHUDBorderLocator.DRAW_REGISTRANT_ID,
                                                      DDHUDBorderDrawOverride.creator)
    except:
        om.MGlobal.displayError("Failed to register draw override: {0}".format(DDHUDDrawOverride.NAME))

def uninitializePlugin(obj):
    """
    """
    pluginFn = om.MFnPlugin(obj)

    try:
        omr.MDrawRegistry.deregisterDrawOverrideCreator(DDHUDLocator.DRAW_DB_CLASSIFICATION,
                                                        DDHUDLocator.DRAW_REGISTRANT_ID)
        omr.MDrawRegistry.deregisterDrawOverrideCreator(DDHUDBorderLocator.DRAW_DB_CLASSIFICATION,
                                                        DDHUDBorderLocator.DRAW_REGISTRANT_ID)
    except:
        om.MGlobal.displayError("Failed to deregister draw override: {0}".format(DDHUDDrawOverride.NAME))

    try:
        pluginFn.deregisterNode(DDHUDLocator.TYPE_ID)
        pluginFn.deregisterNode(DDHUDBorderLocator.TYPE_ID)
    except:
        om.MGlobal.displayError("Failed to unregister node: {0}".format(DDHUDLocator.NAME))

