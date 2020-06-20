<?xml version = "1.0" encoding = "UTF-8"?> 
   <xsl:stylesheet version = "1.0" 
      xmlns:xsl = "http://www.w3.org/1999/XSL/Transform">
   <xsl:template match = "/">
      <html> 
         <body> 
            <h2>projects</h2>
            test
            <p>dd</p>
            <xsl:apply-templates/>
               <!--xsl:for-each select = "Document/Project"-->
               <xsl:for-each select = "Project">
               <p>prj:</p> 
                 <xsl:value-of select = "@name"/>
               </xsl:for-each> 
               <xsl:for-each select = "*/PlantHierarchyFolder"> 
                 <xsl:value-of select = "AttributeList/Attribute/Value"/>
                 <xsl:value-of select = "AttributeList/ProcessTagType"/>
               </xsl:for-each> 
         </body> 
      </html> 
   </xsl:template>  

   <xsl:template match = "Project">
                 <xsl:value-of select = "@Name"/>
   </xsl:template>  
</xsl:stylesheet>