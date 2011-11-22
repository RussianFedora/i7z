#!/bin/bash

ORIGNAME=i7z
VERSION=0.28
SVN_REVISION=71
NAME=${ORIGNAME}-${VERSION}.svn${SVN_REVISION}

rm -rf ${ORIGNAME}
svn co -r $SVN_REVISION http://i7z.googlecode.com/svn/trunk/ i7z >/dev/null
find ${ORIGNAME} -name ".svn" -exec rm -rf {} \; 2>/dev/null
mv ${ORIGNAME} ${NAME}

tar cfJ ${NAME}.tar.xz ${NAME}
rm -rf ${NAME}
