  """  self.w = gl.GLViewWidget()
        self.w.setGeometry(0, 110, 1920, 1080 )
        self.w.show()
        self.nsteps = 1
        self.ypoints = range(-20, 22, self.nsteps)
        self.xpoints = range(-20, 22, self.nsteps)
        self.nfaces = len(self.ypoints)
        self.offset = 0
        self.tmp = OpenSimplex()
        verts = np.array([
            [
                x, y, 1.5 * self.tmp.noise2d(x=n / 5, y=m / 5)
            ] for n, x in enumerate(self.xpoints) for m, y in enumerate(self.ypoints)
        ], dtype=np.float32)
        faces = []
        colors = []
        for m in range(self.nfaces - 1):
            yoff = m * self.nfaces
            for n in range(self.nfaces - 1):
                faces.append([n + yoff, yoff + n + self.nfaces, yoff + n + self.nfaces + 1])
                faces.append([n + yoff, yoff + n + 1, yoff + n + self.nfaces + 1])
                colors.append([0, 0, 0, 0])
                colors.append([0, 0, 0, 0])

        faces = np.array(faces)
        colors = np.array(colors)
        
        # create the mesh item
        self.m1 = gl.GLMeshItem(
            vertexes=verts,
            faces=faces, faceColors=colors,
            smooth=False, drawEdges=True,
        )
        self.m1.setGLOptions('additive')
        self.w.addItem(self.m1)"""
