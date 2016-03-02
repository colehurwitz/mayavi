# Automatically generated code: EDIT AT YOUR OWN RISK
from traits import api as traits
from traitsui import api as traitsui

from tvtk import vtk_module as vtk
from tvtk import tvtk_base
from tvtk.tvtk_base_handler import TVTKBaseHandler
from tvtk import messenger
from tvtk.tvtk_base import deref_vtk
from tvtk import array_handler
from tvtk.array_handler import deref_array
from tvtk.tvtk_classes.tvtk_helper import wrap_vtk

from tvtk.tvtk_classes.image_reader2 import ImageReader2


class PNGReader(ImageReader2):
    """
    PNGReader - read PNG files
    
    Superclass: ImageReader2
    
    PNGReader is a source object that reads PNG files. It should be
    able to read most any PNG file
    
    See Also:
    
    PNGWriter
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPNGReader, obj, update, **traits)
    
    _updateable_traits_ = \
    (('number_of_scalar_components', 'GetNumberOfScalarComponents'),
    ('file_name_slice_offset', 'GetFileNameSliceOffset'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('data_extent',
    'GetDataExtent'), ('file_name', 'GetFileName'), ('data_byte_order',
    'GetDataByteOrder'), ('swap_bytes', 'GetSwapBytes'), ('progress_text',
    'GetProgressText'), ('file_pattern', 'GetFilePattern'),
    ('file_prefix', 'GetFilePrefix'), ('debug', 'GetDebug'),
    ('file_name_slice_spacing', 'GetFileNameSliceSpacing'),
    ('abort_execute', 'GetAbortExecute'), ('header_size',
    'GetHeaderSize'), ('data_spacing', 'GetDataSpacing'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('reference_count',
    'GetReferenceCount'), ('progress', 'GetProgress'), ('file_lower_left',
    'GetFileLowerLeft'), ('data_origin', 'GetDataOrigin'),
    ('file_dimensionality', 'GetFileDimensionality'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'file_lower_left',
    'global_warning_display', 'release_data_flag', 'swap_bytes',
    'data_byte_order', 'data_extent', 'data_origin', 'data_spacing',
    'file_dimensionality', 'file_name', 'file_name_slice_offset',
    'file_name_slice_spacing', 'file_pattern', 'file_prefix',
    'header_size', 'number_of_scalar_components', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(PNGReader, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit PNGReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['file_lower_left', 'swap_bytes'], ['data_byte_order'],
            ['data_extent', 'data_origin', 'data_spacing', 'file_dimensionality',
            'file_name', 'file_name_slice_offset', 'file_name_slice_spacing',
            'file_pattern', 'file_prefix', 'header_size',
            'number_of_scalar_components']),
            title='Edit PNGReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit PNGReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            
