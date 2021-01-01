# trace generated using paraview version 5.6.0
#
# To ensure correct image size when batch processing, please search 
# for and uncomment the line `# renderView*.ViewSize = [*,*]`

import sys
#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'OpenFOAMReader'
test_bestfitfoam = OpenFOAMReader(FileName=sys.argv[1]+'/test_bestfit.foam')
test_bestfitfoam.MeshRegions = ['internalMesh', 'sic/internalMesh', 'forkrod/internalMesh', 'casi/internalMesh', 'fluid/internalMesh', 'chamber/internalMesh', 'air/internalMesh', 'bord/internalMesh', 'anode/internalMesh', 'cover/internalMesh', 'fork/internalMesh', 'collectorbar/internalMesh', 'cathode/internalMesh', 'schamotte/internalMesh', 'global/internalMesh', 'beton/internalMesh']
test_bestfitfoam.CellArrays = ['CpGlobal', 'Epot', 'Epot0', 'J', 'J0', 'T', 'Tcorr', 'U', 'alpha.el', 'alpha1', 'alphaEff', 'isFluid', 'joule', 'kappa', 'lambda', 'melt', 'meltAl', 'p', 'p_rgh', 'peclet', 'rho', 'rhoGlobal', 'sigma']

# get animation scene
animationScene1 = GetAnimationScene()

# update animation scene based on data timesteps
animationScene1.UpdateAnimationUsingDataTimeSteps()

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [960, 414]

# show data in view
test_bestfitfoamDisplay = Show(test_bestfitfoam, renderView1)

# get color transfer function/color map for 'p'
pLUT = GetColorTransferFunction('p')

# get opacity transfer function/opacity map for 'p'
pPWF = GetOpacityTransferFunction('p')

# trace defaults for the display properties.
test_bestfitfoamDisplay.Representation = 'Surface'
test_bestfitfoamDisplay.ColorArrayName = ['POINTS', 'p']
test_bestfitfoamDisplay.LookupTable = pLUT
test_bestfitfoamDisplay.OSPRayScaleArray = 'p'
test_bestfitfoamDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
test_bestfitfoamDisplay.SelectOrientationVectors = 'CpGlobal'
test_bestfitfoamDisplay.ScaleFactor = 0.41669998168945316
test_bestfitfoamDisplay.SelectScaleArray = 'p'
test_bestfitfoamDisplay.GlyphType = 'Arrow'
test_bestfitfoamDisplay.GlyphTableIndexArray = 'p'
test_bestfitfoamDisplay.GaussianRadius = 0.020834999084472658
test_bestfitfoamDisplay.SetScaleArray = ['POINTS', 'p']
test_bestfitfoamDisplay.ScaleTransferFunction = 'PiecewiseFunction'
test_bestfitfoamDisplay.OpacityArray = ['POINTS', 'p']
test_bestfitfoamDisplay.OpacityTransferFunction = 'PiecewiseFunction'
test_bestfitfoamDisplay.DataAxesGrid = 'GridAxesRepresentation'
test_bestfitfoamDisplay.SelectionCellLabelFontFile = ''
test_bestfitfoamDisplay.SelectionPointLabelFontFile = ''
test_bestfitfoamDisplay.PolarAxes = 'PolarAxesRepresentation'
test_bestfitfoamDisplay.ScalarOpacityFunction = pPWF
test_bestfitfoamDisplay.ScalarOpacityUnitDistance = 0.037252466764815126

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
test_bestfitfoamDisplay.DataAxesGrid.XTitleColor = [0.0, 0.0, 0.0]
test_bestfitfoamDisplay.DataAxesGrid.XTitleFontFile = ''
test_bestfitfoamDisplay.DataAxesGrid.YTitleColor = [0.0, 0.0, 0.0]
test_bestfitfoamDisplay.DataAxesGrid.YTitleFontFile = ''
test_bestfitfoamDisplay.DataAxesGrid.ZTitleColor = [0.0, 0.0, 0.0]
test_bestfitfoamDisplay.DataAxesGrid.ZTitleFontFile = ''
test_bestfitfoamDisplay.DataAxesGrid.XLabelColor = [0.0, 0.0, 0.0]
test_bestfitfoamDisplay.DataAxesGrid.XLabelFontFile = ''
test_bestfitfoamDisplay.DataAxesGrid.YLabelColor = [0.0, 0.0, 0.0]
test_bestfitfoamDisplay.DataAxesGrid.YLabelFontFile = ''
test_bestfitfoamDisplay.DataAxesGrid.ZLabelColor = [0.0, 0.0, 0.0]
test_bestfitfoamDisplay.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
test_bestfitfoamDisplay.PolarAxes.PolarAxisTitleColor = [0.0, 0.0, 0.0]
test_bestfitfoamDisplay.PolarAxes.PolarAxisTitleFontFile = ''
test_bestfitfoamDisplay.PolarAxes.PolarAxisLabelColor = [0.0, 0.0, 0.0]
test_bestfitfoamDisplay.PolarAxes.PolarAxisLabelFontFile = ''
test_bestfitfoamDisplay.PolarAxes.LastRadialAxisTextColor = [0.0, 0.0, 0.0]
test_bestfitfoamDisplay.PolarAxes.LastRadialAxisTextFontFile = ''
test_bestfitfoamDisplay.PolarAxes.SecondaryRadialAxesTextColor = [0.0, 0.0, 0.0]
test_bestfitfoamDisplay.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# reset view to fit data
renderView1.ResetCamera()

# show color bar/color legend
test_bestfitfoamDisplay.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on test_bestfitfoam
test_bestfitfoam.MeshRegions = ['fork/internalMesh']

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on test_bestfitfoamDisplay
test_bestfitfoamDisplay.SelectOrientationVectors = 'Epot0'

animationScene1.GoToLast()

# reset view to fit data
renderView1.ResetCamera()

# Properties modified on test_bestfitfoam
test_bestfitfoam.MeshRegions = ['fluid/internalMesh']

# update the view to ensure updated data information
renderView1.Update()

# reset view to fit data
renderView1.ResetCamera()

# create a new 'Slice'
slice1 = Slice(Input=test_bestfitfoam)
slice1.SliceType = 'Plane'
slice1.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice1.SliceType.Origin = [-0.9775000214576721, 0.1420000046491623, 0.9820000231266022]

# Properties modified on slice1.SliceType
slice1.SliceType.Normal = [0.0, 1.0, 0.0]

# Properties modified on slice1.SliceType
slice1.SliceType.Normal = [0.0, 1.0, 0.0]

# show data in view
slice1Display = Show(slice1, renderView1)

# trace defaults for the display properties.
slice1Display.Representation = 'Surface'
slice1Display.ColorArrayName = ['POINTS', 'p']
slice1Display.LookupTable = pLUT
slice1Display.OSPRayScaleArray = 'p'
slice1Display.OSPRayScaleFunction = 'PiecewiseFunction'
slice1Display.SelectOrientationVectors = 'U'
slice1Display.ScaleFactor = 0.19550000429153444
slice1Display.SelectScaleArray = 'p'
slice1Display.GlyphType = 'Arrow'
slice1Display.GlyphTableIndexArray = 'p'
slice1Display.GaussianRadius = 0.009775000214576722
slice1Display.SetScaleArray = ['POINTS', 'p']
slice1Display.ScaleTransferFunction = 'PiecewiseFunction'
slice1Display.OpacityArray = ['POINTS', 'p']
slice1Display.OpacityTransferFunction = 'PiecewiseFunction'
slice1Display.DataAxesGrid = 'GridAxesRepresentation'
slice1Display.SelectionCellLabelFontFile = ''
slice1Display.SelectionPointLabelFontFile = ''
slice1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
slice1Display.DataAxesGrid.XTitleColor = [0.0, 0.0, 0.0]
slice1Display.DataAxesGrid.XTitleFontFile = ''
slice1Display.DataAxesGrid.YTitleColor = [0.0, 0.0, 0.0]
slice1Display.DataAxesGrid.YTitleFontFile = ''
slice1Display.DataAxesGrid.ZTitleColor = [0.0, 0.0, 0.0]
slice1Display.DataAxesGrid.ZTitleFontFile = ''
slice1Display.DataAxesGrid.XLabelColor = [0.0, 0.0, 0.0]
slice1Display.DataAxesGrid.XLabelFontFile = ''
slice1Display.DataAxesGrid.YLabelColor = [0.0, 0.0, 0.0]
slice1Display.DataAxesGrid.YLabelFontFile = ''
slice1Display.DataAxesGrid.ZLabelColor = [0.0, 0.0, 0.0]
slice1Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
slice1Display.PolarAxes.PolarAxisTitleColor = [0.0, 0.0, 0.0]
slice1Display.PolarAxes.PolarAxisTitleFontFile = ''
slice1Display.PolarAxes.PolarAxisLabelColor = [0.0, 0.0, 0.0]
slice1Display.PolarAxes.PolarAxisLabelFontFile = ''
slice1Display.PolarAxes.LastRadialAxisTextColor = [0.0, 0.0, 0.0]
slice1Display.PolarAxes.LastRadialAxisTextFontFile = ''
slice1Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0, 0.0, 0.0]
slice1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# hide data in view
Hide(test_bestfitfoam, renderView1)

# show color bar/color legend
slice1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(slice1Display, ('CELLS', 'melt'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(pLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
slice1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
slice1Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'melt'
meltLUT = GetColorTransferFunction('melt')

# get opacity transfer function/opacity map for 'melt'
meltPWF = GetOpacityTransferFunction('melt')

# set active source
SetActiveSource(test_bestfitfoam)

# set active source
SetActiveSource(slice1)

# rename source object
RenameSource('Melt', slice1)

# set active source
SetActiveSource(test_bestfitfoam)

# current camera placement for renderView1
renderView1.CameraPosition = [-0.9775000214576721, -3.740772504398338, 0.9820000231266022]
renderView1.CameraFocalPoint = [-0.9775000214576721, 0.1420000046491623, 0.9820000231266022]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 1.0049354731419926

# save screenshot
SaveScreenshot(sys.argv[2]+'/melt.jpeg', renderView1, ImageResolution=[960, 414], 
    # JPEG options
    Quality=100)

# create a new 'Slice'
slice1_1 = Slice(Input=test_bestfitfoam)
slice1_1.SliceType = 'Plane'
slice1_1.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice1_1.SliceType.Origin = [-0.9775000214576721, 0.1420000046491623, 0.9820000231266022]

# Properties modified on slice1_1.SliceType
slice1_1.SliceType.Normal = [0.0, 1.0, 0.0]

# Properties modified on slice1_1.SliceType
slice1_1.SliceType.Normal = [0.0, 1.0, 0.0]

# show data in view
slice1_1Display = Show(slice1_1, renderView1)

# trace defaults for the display properties.
slice1_1Display.Representation = 'Surface'
slice1_1Display.ColorArrayName = ['POINTS', 'p']
slice1_1Display.LookupTable = pLUT
slice1_1Display.OSPRayScaleArray = 'p'
slice1_1Display.OSPRayScaleFunction = 'PiecewiseFunction'
slice1_1Display.SelectOrientationVectors = 'U'
slice1_1Display.ScaleFactor = 0.19550000429153444
slice1_1Display.SelectScaleArray = 'p'
slice1_1Display.GlyphType = 'Arrow'
slice1_1Display.GlyphTableIndexArray = 'p'
slice1_1Display.GaussianRadius = 0.009775000214576722
slice1_1Display.SetScaleArray = ['POINTS', 'p']
slice1_1Display.ScaleTransferFunction = 'PiecewiseFunction'
slice1_1Display.OpacityArray = ['POINTS', 'p']
slice1_1Display.OpacityTransferFunction = 'PiecewiseFunction'
slice1_1Display.DataAxesGrid = 'GridAxesRepresentation'
slice1_1Display.SelectionCellLabelFontFile = ''
slice1_1Display.SelectionPointLabelFontFile = ''
slice1_1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
slice1_1Display.DataAxesGrid.XTitleColor = [0.0, 0.0, 0.0]
slice1_1Display.DataAxesGrid.XTitleFontFile = ''
slice1_1Display.DataAxesGrid.YTitleColor = [0.0, 0.0, 0.0]
slice1_1Display.DataAxesGrid.YTitleFontFile = ''
slice1_1Display.DataAxesGrid.ZTitleColor = [0.0, 0.0, 0.0]
slice1_1Display.DataAxesGrid.ZTitleFontFile = ''
slice1_1Display.DataAxesGrid.XLabelColor = [0.0, 0.0, 0.0]
slice1_1Display.DataAxesGrid.XLabelFontFile = ''
slice1_1Display.DataAxesGrid.YLabelColor = [0.0, 0.0, 0.0]
slice1_1Display.DataAxesGrid.YLabelFontFile = ''
slice1_1Display.DataAxesGrid.ZLabelColor = [0.0, 0.0, 0.0]
slice1_1Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
slice1_1Display.PolarAxes.PolarAxisTitleColor = [0.0, 0.0, 0.0]
slice1_1Display.PolarAxes.PolarAxisTitleFontFile = ''
slice1_1Display.PolarAxes.PolarAxisLabelColor = [0.0, 0.0, 0.0]
slice1_1Display.PolarAxes.PolarAxisLabelFontFile = ''
slice1_1Display.PolarAxes.LastRadialAxisTextColor = [0.0, 0.0, 0.0]
slice1_1Display.PolarAxes.LastRadialAxisTextFontFile = ''
slice1_1Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0, 0.0, 0.0]
slice1_1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# hide data in view
Hide(test_bestfitfoam, renderView1)

# show color bar/color legend
slice1_1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# rename source object
RenameSource('meltAl', slice1_1)

# set scalar coloring
ColorBy(slice1_1Display, ('CELLS', 'meltAl'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(pLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
slice1_1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
slice1_1Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'meltAl'
meltAlLUT = GetColorTransferFunction('meltAl')

# get opacity transfer function/opacity map for 'meltAl'
meltAlPWF = GetOpacityTransferFunction('meltAl')

# set active source
SetActiveSource(test_bestfitfoam)

# hide data in view
Hide(slice1, renderView1)

# set active source
SetActiveSource(slice1_1)

# set active source
SetActiveSource(test_bestfitfoam)

# current camera placement for renderView1
renderView1.CameraPosition = [-0.9775000214576721, -3.740772504398338, 0.9820000231266022]
renderView1.CameraFocalPoint = [-0.9775000214576721, 0.1420000046491623, 0.9820000231266022]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 1.0049354731419926

# save screenshot
SaveScreenshot(sys.argv[2]+'/meltAl.jpeg', renderView1, ImageResolution=[960, 414])

# hide data in view
Hide(slice1_1, renderView1)

# create a new 'Slice'
slice1_2 = Slice(Input=test_bestfitfoam)
slice1_2.SliceType = 'Plane'
slice1_2.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice1_2.SliceType.Origin = [-0.9775000214576721, 0.1420000046491623, 0.9820000231266022]

# Properties modified on slice1_2.SliceType
slice1_2.SliceType.Normal = [0.0, 1.0, 0.0]

# Properties modified on slice1_2.SliceType
slice1_2.SliceType.Normal = [0.0, 1.0, 0.0]

# show data in view
slice1_2Display = Show(slice1_2, renderView1)

# trace defaults for the display properties.
slice1_2Display.Representation = 'Surface'
slice1_2Display.ColorArrayName = ['POINTS', 'p']
slice1_2Display.LookupTable = pLUT
slice1_2Display.OSPRayScaleArray = 'p'
slice1_2Display.OSPRayScaleFunction = 'PiecewiseFunction'
slice1_2Display.SelectOrientationVectors = 'U'
slice1_2Display.ScaleFactor = 0.19550000429153444
slice1_2Display.SelectScaleArray = 'p'
slice1_2Display.GlyphType = 'Arrow'
slice1_2Display.GlyphTableIndexArray = 'p'
slice1_2Display.GaussianRadius = 0.009775000214576722
slice1_2Display.SetScaleArray = ['POINTS', 'p']
slice1_2Display.ScaleTransferFunction = 'PiecewiseFunction'
slice1_2Display.OpacityArray = ['POINTS', 'p']
slice1_2Display.OpacityTransferFunction = 'PiecewiseFunction'
slice1_2Display.DataAxesGrid = 'GridAxesRepresentation'
slice1_2Display.SelectionCellLabelFontFile = ''
slice1_2Display.SelectionPointLabelFontFile = ''
slice1_2Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
slice1_2Display.DataAxesGrid.XTitleColor = [0.0, 0.0, 0.0]
slice1_2Display.DataAxesGrid.XTitleFontFile = ''
slice1_2Display.DataAxesGrid.YTitleColor = [0.0, 0.0, 0.0]
slice1_2Display.DataAxesGrid.YTitleFontFile = ''
slice1_2Display.DataAxesGrid.ZTitleColor = [0.0, 0.0, 0.0]
slice1_2Display.DataAxesGrid.ZTitleFontFile = ''
slice1_2Display.DataAxesGrid.XLabelColor = [0.0, 0.0, 0.0]
slice1_2Display.DataAxesGrid.XLabelFontFile = ''
slice1_2Display.DataAxesGrid.YLabelColor = [0.0, 0.0, 0.0]
slice1_2Display.DataAxesGrid.YLabelFontFile = ''
slice1_2Display.DataAxesGrid.ZLabelColor = [0.0, 0.0, 0.0]
slice1_2Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
slice1_2Display.PolarAxes.PolarAxisTitleColor = [0.0, 0.0, 0.0]
slice1_2Display.PolarAxes.PolarAxisTitleFontFile = ''
slice1_2Display.PolarAxes.PolarAxisLabelColor = [0.0, 0.0, 0.0]
slice1_2Display.PolarAxes.PolarAxisLabelFontFile = ''
slice1_2Display.PolarAxes.LastRadialAxisTextColor = [0.0, 0.0, 0.0]
slice1_2Display.PolarAxes.LastRadialAxisTextFontFile = ''
slice1_2Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0, 0.0, 0.0]
slice1_2Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# reset view to fit data
renderView1.ResetCamera()

#changing interaction mode based on data extents
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [-0.9775000214576721, 10000.14200000465, 0.9820000231266022]
renderView1.CameraViewUp = [1.0, 0.0, 0.0]

# hide data in view
Hide(test_bestfitfoam, renderView1)

# show color bar/color legend
slice1_2Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# reset view to fit data
renderView1.ResetCamera()

#change interaction mode for render view
renderView1.InteractionMode = '3D'

# set scalar coloring
ColorBy(slice1_2Display, ('CELLS', 'T'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(pLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
slice1_2Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
slice1_2Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'T'
tLUT = GetColorTransferFunction('T')

# get opacity transfer function/opacity map for 'T'
tPWF = GetOpacityTransferFunction('T')

# rename source object
RenameSource('T', slice1_2)

# set active source
SetActiveSource(test_bestfitfoam)

# current camera placement for renderView1
renderView1.CameraPosition = [-0.9775000885128975, -2.9639027466683365, 0.9820000529289246]
renderView1.CameraFocalPoint = [-0.9775000885128975, 0.1419999897480011, 0.9820000529289246]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 1.4240990373886686

# save screenshot
SaveScreenshot(sys.argv[2]+'/T.jpeg', renderView1, ImageResolution=[960, 414])

# hide data in view
Hide(slice1_2, renderView1)

# set active source
SetActiveSource(test_bestfitfoam)

# show data in view
test_bestfitfoamDisplay = Show(test_bestfitfoam, renderView1)

# show color bar/color legend
test_bestfitfoamDisplay.SetScalarBarVisibility(renderView1, True)

# reset view to fit data
renderView1.ResetCamera()

# create a new 'Slice'
slice1_3 = Slice(Input=test_bestfitfoam)
slice1_3.SliceType = 'Plane'
slice1_3.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice1_3.SliceType.Origin = [-0.9775000214576721, 0.1420000046491623, 0.9820000231266022]

# Properties modified on slice1_3.SliceType
slice1_3.SliceType.Normal = [0.0, 1.0, 0.0]

# Properties modified on slice1_3.SliceType
slice1_3.SliceType.Normal = [0.0, 1.0, 0.0]

# show data in view
slice1_3Display = Show(slice1_3, renderView1)

# trace defaults for the display properties.
slice1_3Display.Representation = 'Surface'
slice1_3Display.ColorArrayName = ['POINTS', 'p']
slice1_3Display.LookupTable = pLUT
slice1_3Display.OSPRayScaleArray = 'p'
slice1_3Display.OSPRayScaleFunction = 'PiecewiseFunction'
slice1_3Display.SelectOrientationVectors = 'U'
slice1_3Display.ScaleFactor = 0.19550000429153444
slice1_3Display.SelectScaleArray = 'p'
slice1_3Display.GlyphType = 'Arrow'
slice1_3Display.GlyphTableIndexArray = 'p'
slice1_3Display.GaussianRadius = 0.009775000214576722
slice1_3Display.SetScaleArray = ['POINTS', 'p']
slice1_3Display.ScaleTransferFunction = 'PiecewiseFunction'
slice1_3Display.OpacityArray = ['POINTS', 'p']
slice1_3Display.OpacityTransferFunction = 'PiecewiseFunction'
slice1_3Display.DataAxesGrid = 'GridAxesRepresentation'
slice1_3Display.SelectionCellLabelFontFile = ''
slice1_3Display.SelectionPointLabelFontFile = ''
slice1_3Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
slice1_3Display.DataAxesGrid.XTitleColor = [0.0, 0.0, 0.0]
slice1_3Display.DataAxesGrid.XTitleFontFile = ''
slice1_3Display.DataAxesGrid.YTitleColor = [0.0, 0.0, 0.0]
slice1_3Display.DataAxesGrid.YTitleFontFile = ''
slice1_3Display.DataAxesGrid.ZTitleColor = [0.0, 0.0, 0.0]
slice1_3Display.DataAxesGrid.ZTitleFontFile = ''
slice1_3Display.DataAxesGrid.XLabelColor = [0.0, 0.0, 0.0]
slice1_3Display.DataAxesGrid.XLabelFontFile = ''
slice1_3Display.DataAxesGrid.YLabelColor = [0.0, 0.0, 0.0]
slice1_3Display.DataAxesGrid.YLabelFontFile = ''
slice1_3Display.DataAxesGrid.ZLabelColor = [0.0, 0.0, 0.0]
slice1_3Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
slice1_3Display.PolarAxes.PolarAxisTitleColor = [0.0, 0.0, 0.0]
slice1_3Display.PolarAxes.PolarAxisTitleFontFile = ''
slice1_3Display.PolarAxes.PolarAxisLabelColor = [0.0, 0.0, 0.0]
slice1_3Display.PolarAxes.PolarAxisLabelFontFile = ''
slice1_3Display.PolarAxes.LastRadialAxisTextColor = [0.0, 0.0, 0.0]
slice1_3Display.PolarAxes.LastRadialAxisTextFontFile = ''
slice1_3Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0, 0.0, 0.0]
slice1_3Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# hide data in view
Hide(test_bestfitfoam, renderView1)

# show color bar/color legend
slice1_3Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# rename source object
RenameSource('sigma', slice1_3)

# set scalar coloring
ColorBy(slice1_3Display, ('CELLS', 'sigma'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(pLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
slice1_3Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
slice1_3Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'sigma'
sigmaLUT = GetColorTransferFunction('sigma')

# get opacity transfer function/opacity map for 'sigma'
sigmaPWF = GetOpacityTransferFunction('sigma')

# set active source
SetActiveSource(test_bestfitfoam)

# current camera placement for renderView1
renderView1.CameraPosition = [-0.9775000214576721, -3.740772504398338, 0.9820000231266022]
renderView1.CameraFocalPoint = [-0.9775000214576721, 0.1420000046491623, 0.9820000231266022]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 1.0049354731419926

# save screenshot
SaveScreenshot(sys.argv[2]+'/sigma.jpeg', renderView1, ImageResolution=[960, 414])

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [-0.9775000214576721, -3.740772504398338, 0.9820000231266022]
renderView1.CameraFocalPoint = [-0.9775000214576721, 0.1420000046491623, 0.9820000231266022]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 1.0049354731419926

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).
