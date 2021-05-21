<!-- The Identity Transformation -->
<xsl:stylesheet version="2.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:tei="http://www.tei-c.org/ns/1.0" xpath-default-namespace="http://www.tei-c.org/ns/1.0">
    <!-- Whenever you match any node or any attribute -->
    <xsl:template match="node()|@*">
        <!-- Copy the current node -->
        <xsl:copy>
            <!-- Including any attributes it has and any child nodes -->
            <xsl:apply-templates select="@*"/>
            <xsl:apply-templates/>
        </xsl:copy>
    </xsl:template>
    
    <!-- requiert qu'on ajoute manuellement l'attribut n="1" au premier paragraphe du texte -->
    
    <xsl:template name="plusun">
        <xsl:param name="lastn" select="1"/>
        <xsl:choose>
            <xsl:when test="preceding::p[$lastn][@n]">
                <xsl:value-of select="$lastn + 1"/>
            </xsl:when>
            <xsl:otherwise>
                <xsl:call-template name="plusun">
                    <xsl:with-param name="lastn" select ="$lastn + 1"/>
                </xsl:call-template>
            </xsl:otherwise>
        </xsl:choose>
    </xsl:template>
    
    <xsl:template match="text//p[not(@n)]">
        <xsl:copy>
            <xsl:attribute name="n">
                <xsl:call-template name="plusun">
                    <xsl:with-param name="lastn" select="1"/>
                </xsl:call-template>
            </xsl:attribute>
            <xsl:apply-templates select="@*"/>
            <xsl:apply-templates/>
        </xsl:copy>
    </xsl:template>
    
    <xsl:template match="@part"/>
    
</xsl:stylesheet>