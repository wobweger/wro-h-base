<?xml version = "1.0" encoding = "UTF-8"?> 
   <xsl:stylesheet version = "1.0" 
      xmlns:xsl = "http://www.w3.org/1999/XSL/Transform">
<!--xsl:output method="html"/-->
<xsl:output method="text"/>
<!-- root 
  -->
<xsl:template match = "/">
   <xsl:apply-templates select="Document/Project"/>
      <html> 
         <body> 
            <h2>projects</h2>
            test
            <p>dd</p>
               <!--xsl:for-each select = "Document/Project"-->
               <xsl:for-each select = "Project">
               <p>prj:</p> 
                 <xsl:value-of select = "@Name"/>
               </xsl:for-each> 
         </body> 
      </html> 
   </xsl:template>  

<!-- find project 
  -->
<xsl:template match="Project">
   <xsl:text>prj:</xsl:text>
   <xsl:value-of select="@Name"/>
   <xsl:text>
</xsl:text>

</xsl:template>  
</xsl:stylesheet>