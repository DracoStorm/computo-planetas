# Librería cv2

<p align="center">
  <img src="opencv.png">
</p>

Se utiliza a menudo para el procesamiento de imágenes y vídeo. Proporciona a los desarrolladores una interfaz fácil de usar para trabajar con funciones de procesamiento de imágenes y vídeo. Es por esto que en nuestros códigos que requirieron generar imágenes para la animación final, recurrimos a ésta.




## Lo más importante

Una biblioteca, tal como lo indica el nombre, es gigante, pero a continuación listaré un par de las funciones más importantes y usadas de OpenCV. No obstante, más abajo se listan todas y cada una de ellas.

1.  cv2.imread():

    Es una función para leer una imagen de un archivo. Toma la ruta del archivo como entrada y devuelve un array numpy que contiene la imagen. 

2.  cv2.resize():

    Es una función que se utiliza para cambiar el tamaño de una imagen. Toma la imagen de entrada y las nuevas dimensiones como entradas y devuelve la imagen redimensionada.

3.  cv2.imshow():

    Es una función utilizada para mostrar una imagen. Toma la imagen como entrada y abre una nueva ventana para mostrar la imagen. 

4.  cv2.imwrite():

    Es una función para guardar una imagen en un archivo. Toma la imagen y la ruta del archivo como entrada y guarda la imagen en la ruta del archivo.

5.  cv2.threshold():

    Es una función que se puede utilizar para umbralizar una imagen. Toma la imagen de entrada y un valor umbral como entrada y devuelve la imagen umbralizada. A continuación, un ejemplo para clarificar:

    ![ejemplo](cv.thresh.jpg)

6.  cv2.rectangle():

    Es una función para dibujar un rectángulo en una imagen. Toma la imagen de entrada, las coordenadas del rectángulo, el color y el grosor como entradas y devuelve la imagen con el rectángulo dibujado.

7.  cv2.findContours():

    Es una función que se utiliza para encontrar los contornos en una imagen. Toma la imagen de entrada, el modo de recuperación del contorno y el método de aproximación del contorno como entradas y devuelve los contornos. 



### Todo el contenido

cv2.absdiff                 <br>
cv2.accumulate<br>
cv2.accumulateProduct<br>
cv2.accumulateSquare<br>
cv2.accumulateWeighted<br>
cv2.adaptiveThreshold<br>
cv2.add<br>
cv2.addText<br>
cv2.addWeighted<br>
cv2.applyColorMap<br>
cv2.approxPolyDP<br>
cv2.arcLength<br>
cv2.arrowedLine<br>
cv2.batchDistance<br>
cv2.bilateralFilter<br>
cv2.bitwise_and<br>
cv2.bitwise_not<br>
cv2.bitwise_or<br>
cv2.bitwise_xor<br>
cv2.blur<br>
cv2.boundingRect<br>
cv2.boxFilter<br>
cv2.boxPoints<br>
cv2.buildOpticalFlowPyramid<br>
cv2.calcBackProject<br>
cv2.calcCovarMatrix<br>
cv2.calcHist<br>
cv2.calcOpticalFlowFarneback<br>
cv2.calcOpticalFlowPyrLK<br>
cv2.calibrateCamera<br>
cv2.calibrationMatrixValues<br>
cv2.CamShift<br>
cv2.Canny<br>
cv2.cartToPolar<br>
cv2.CascadeClassifier<br>
cv2.circle<br>
cv2.clipLine<br>
cv2.colorChange<br>
cv2.compare<br>
cv2.compareHist<br>
cv2.completeSymm<br>
cv2.composeRT<br>
cv2.computeCorrespondEpiline<br>
cv2.connectedComponents<br>
cv2.connectedComponentsWithStats    <br>
cv2.contourArea<br>
cv2.convertMaps<br>
cv2.convertPointsFromHomogeneous<br>
cv2.convertPointsToHomogeneous<br>
cv2.convertScaleAbs<br>
cv2.convexHull<br>
cv2.convexityDefects<br>
cv2.copyMakeBorder<br>
cv2.cornerEigenValsAndVecs<br>
cv2.cornerHarris<br>
cv2.cornerMinEigenVal<br>
cv2.cornerSubPix<br>
cv2.cornerEigenValsAndVecs<br>
cv2.cornerMinEigenVal<br>
cv2.cornerSubPix<br>
cv2.createAlignMTB<br>
cv2.createBackgroundSubtractorKNN<br>
cv2.createBackgroundSubtractorMOG2<br>
cv2.createButton<br>
cv2.createCLAHE<br>
cv2.createLineSegmentDetector<br>
cv2.createMergeDebevec<br>
cv2.createMergeMertens<br>
cv2.createMergeRobertson<br>
cv2.createTonemap<br>
cv2.createTonemapDrago<br>
cv2.createTonemapMantiuk<br>
cv2.createTonemapReinhard<br>
cv2.cvtColor<br>
cv2.dct<br>
cv2.decolor<br>
cv2.demosaicing<br>
cv2.destroyAllWindows<br>
cv2.destroyWindow<br>
cv2.detailEnhance<br>
cv2.detail_HomographyBasedEstimator<br>
cv2.detail_BestOf2NearestMatcher<br>
cv2.detail_BestOf2NearestRangeMatcher<br>
cv2.detail_Blender<br>
cv2.detail_CameraParams<br>
cv2.detail_ChannelsCompensator<br>
cv2.detail_DpSeamFinder<br>
cv2.detail_Estimator<br>
cv2.detail_FeatherBlender<br>
cv2.detail_FeaturesMatcher<br>
cv2.detail_GainCompensator<br>
cv2.detail_GraphCutSeamFinder<br>
cv2.detail_HomographyBasedEsti<br>mator
cv2.detail_Interpolator<br>
cv2.detail_MultiBandBlender<br>
cv2.detail_NoBundleAdjuster<br>
cv2.detail_NoSeamFinder<br>
cv2.detail_SeamFinder<br>
cv2.detail_Timelapser<br>
cv2.detail_TimelapserCrop<br>
cv2.detail_VoronoiSeamFinder<br>
cv2.determinant<br>
cv2.dft<br>
cv2.dilate<br>
cv2.distanceTransform<br>
cv2.distanceTransformWithLabel<br>s
cv2.divide<br>
cv2.drawChessboardCorners<br>
cv2.drawContours<br>
cv2.drawKeypoints<br>
cv2.drawMatches<br>
cv2.drawMatchesKnn<br>
cv2.ellipse<br>
cv2.ellipse2Poly<br>
cv2.equalizeHist<br>
cv2.erode<br>
cv2.error<br>
cv2.estimateAffine2D<br>
cv2.estimateAffine3D<br>
cv2.estimateAffinePartial2D<br>
cv2.estimateRigidTransform<br>
cv2.fastAtan2<br>
cv2.fastNlMeansDenoising<br>
cv2.fastNlMeansDenoisingColored<br>
cv2.fastNlMeansDenoisingColoredMulti<br>
cv2.fastNlMeansDenoisingMulti<br>
cv2.fillConvexPoly<br>
cv2.fillPoly<br>
cv2.filter2D<br>
cv2.findChessboardCorners<br>
cv2.findContours<br>
cv2.findEssentialMat<br>
cv2.findFundamentalMat<br>
cv2.findHomography<br>
cv2.findNonZero<br>
cv2.findTransformECC<br>
cv2.fitEllipse<br>
cv2.fitEllipseAMS<br>
cv2.fitEllipseDirect<br>
cv2.fitLine<br>
cv2.floodFill<br>
cv2.gemm<br>
cv2.getAffineTransform<br>
cv2.getBuildInformation<br>
cv2.getCPUTickCount<br>
cv2.getDefaultNewCameraMatrix<br>
cv2.getDerivKernels<br>
cv2.getGaborKernel<br>
cv2.getGaussianKernel<br>
cv2.getOptimalDFTSize<br>
cv2.getOptimalNewCameraMatrix<br>
cv2.getPerspectiveTransform<br>
cv2.getRectSubPix<br>
cv2.getRotationMatrix2D<br>
cv2.getStructuringElement<br>
cv2.getTextSize<br>
cv2.getTickCount<br>
cv2.getTickFrequency<br>
cv2.getTrackbarPos<br>
cv2.getValidDisparityROI<br>
cv2.getWindowImageRect<br>
cv2.getWindowProperty<br>
cv2.goodFeaturesToTrack<br>
cv2.grabCut<br>
cv2.grab<br>
cv2.haveImageReader<br>
cv2.haveImageWriter<br>
cv2.hconcat<br>
cv2.idct<br>
cv2.idft<br>
cv2.imshow<br>
cv2.imdecode<br>
cv2.imencode<br>
cv2.imread<br>
cv2.imreadmulti<br>
cv2.imshow<br>
cv2.inRange<br>
cv2.initCameraMatrix2D<br>
cv2.initUndistortRectifyMap<br>
cv2.inpaint<br>
cv2.invert<br>
cv2.invertAffineTransform<br>
cv2.isContourConvex<br>
cv2.kmeans<br>
cv2.line<br>
cv2.linearPolar<br>
cv2.log<br>
cv2.logPolar<br>
cv2.LUT<br>
cv2.magnitude<br>
cv2.map<br>
cv2.matchShapes<br>
cv2.matchTemplate<br>
cv2.matMulDeriv<br>
cv2.mean<br>
cv2.meanShift<br>
cv2.meanStdDev<br>
cv2.merge<br>
cv2.minAreaRect<br>
cv2.minEnclosingCircle<br>
cv2.minEnclosingTriangle<br>
cv2.minMaxLoc<br>
cv2.moments<br>
cv2.morphologyEx<br>
cv2.moveWindow<br>
cv2.mulSpectrums<br>
cv2.multiply<br>
cv2.namedWindow<br>
cv2.norm<br>
cv2.normalize<br>
cv2.ORB_create<br>
cv2.ocl<br>
cv2.pencilSketch<br>
cv2.perspectiveTransform<br>
cv2.phase<br>
cv2.phaseCorrel<br>