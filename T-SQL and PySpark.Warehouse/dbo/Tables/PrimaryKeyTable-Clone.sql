CREATE TABLE [dbo].[PrimaryKeyTable-Clone] (

	[c1] int NOT NULL, 
	[c2] int NULL
);


GO
ALTER TABLE [dbo].[PrimaryKeyTable-Clone] ADD CONSTRAINT PK__PrimaryK__3213663A7025A326 primary key NONCLUSTERED ([c1]);