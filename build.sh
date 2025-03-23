#!/bin/bash

clear_public() {
  DIRS="404.html
    categories
    css
    index.html
    index.xml
    LICENSE
    QUIC
    RFC8999_Chinese_Simplified
    RFC8999_Chinese_Translation
    rfc8999-zh-cn
    RFC9000_Chinese_Simplified
    RFC9000_Chinese_Translation
    rfc9000-zh-cn
    RFC9001_Chinese_Simplified
    RFC9001_Chinese_Translation
    rfc9001-zh-cn
    RFC9002_Chinese_Simplified
    RFC9002_Chinese_Translation
    rfc9002-zh-cn
    RFC9114_Chinese_Simplified
    RFC9204_Chinese_Simplified
    RFC9220_Chinese_Simplified
    RFC9221_Chinese_Simplified
    RFC9250_Chinese_Simplified
    RFC9287_Chinese_Simplified
    RFC9308_Chinese_Simplified
    RFC9312_Chinese_Simplified
    RFC9368_Chinese_Simplified
    RFC9369_Chinese_Simplified
    RFC9412_Chinese_Simplified
    RFC9443_Chinese_Simplified
    sitemap.xml
    tags
    test
    Translation_Norms"

  for x in ${DIRS}; do
    rm -rf public/$x
  done
}

clear_public

./scripts/sass.py
hugo
./scripts/remove_p_linebreaks.py
find public -name "*.scss" | xargs rm
