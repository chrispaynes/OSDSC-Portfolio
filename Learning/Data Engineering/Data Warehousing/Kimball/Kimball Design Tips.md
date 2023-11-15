# Tip 168 - What’s in a Name?
Good names for tables and columns are particularly important for ad hoc users of the DW/BI system who need to find the objects they’re looking for. Object names should be oriented to the business users, not the technical staff.

As much as possible, strive to have the names in the DW/BI system be unchanged in the semantic layer and unchanged by report designers. More challenging, your users should be discouraged from changing object names once they’ve pulled the information to their desktop. We usually can’t prevent them from doing that, but attractive and sensible names will reduce the temptation.

Here are my top ten suggestions for naming objects in your data warehouse / business intelligence system.

1. Follow naming conventions.
If you don’t have them, create (and document!) naming conventions that follow the rules in this Design Tip. If your organization already has naming conventions, you may be faced with a problem: most existing naming conventions were developed for technical people. But names in the DW/BI environment should be oriented to the business users. They become row and column names in ad hoc analyses and predefined reports. We will return to this issue later.

2. Each object has one name.
Let’s not perpetuate the confusion around data definitions that already exists in our organizations. It is not OK to say that the sales team can call a column Geography and the marketing group calls the same entity Region. If it’s the same column, with the same content, it has to have the same name. If you can’t get agreement organization-wide on object names, enlist the help of your business sponsor.

3. Object names are descriptive.
Users should not need 20 years tenure at your organization to decipher what a name means. This rule forbids a lot of silliness, like RBVLSPCD (we have more than 8 characters to work with!). It also forbids column names like NAME, which is non-descriptive outside the context of the table you are examining.

4. Abbreviations and acronyms are discouraged.
Abbreviations and acronyms are endemic in the corporate world, and the non-corporate world is even worse. A lot of information can be encoded in an acronym, but it places a huge burden on newcomers. The most effective approach is to maintain a list of approved abbreviations, and try not to add to them without a good reason. You may even want to document that reason in the list. Examples include:
 Abbreviation 	 Replaces 	 Reason
 Amt 	 Amount 	 Extremely common
 Desc 	 Description 	 Extremely common
 Corp 	 Corporation 	 Common
 FDIC 	 Federal Deposit Insurance Corporation 	 Common; familiar to all users

For most organizations, a reasonable list has dozens of approved abbreviations, not hundreds.

5. Object names are pretty.
Remember that object names become headers in reports and analyses. Although beauty is in the eye of the beholder, I find all caps to be particularly annoying. The object names should contain a visual clue for where the words end.

    Spaces: [Column Name]
    Camel case: ColumnName
    Underscore: Column_Name or COLUMN_NAME

I recommend using spaces. They look the best when displayed in reports. And I scoff at the argument that developers have to type square brackets when they type the column name. I am confident that any developer who actually types SQL can figure out where the brackets keys are located, and they can develop the requisite finger muscles.

6. Object names are unique.
This rule is a corollary to the rule that each object has one name. If two objects are different, they should have different names. This rule forbids column names such as [City]. A better name is [Customer Mailing Address City]. This rule is especially important for ad hoc use of the DW/BI system. Although the context of [City] may be obvious during the analytic process, once that analysis is saved and shared, that context is lost. Are we looking at the customer’s city or the store’s city, the mailing address or the shipping address? Although we can’t prevent users from changing object names once they export to Excel, we don’t want to force them to do so in order to be clear.

7. Object names are not too long.
This rule conflicts with rules 3, 4, and 6. If we have unique, unabbreviated, descriptive object names, the odds are that some column names will be very long. Consider [Mandatory Second Payer Letter Opt Out Code] or [Vocational Provider Referral Category]. These are reasonably descriptive column names for someone in the insurance business, but what will happen when the user or report designer drags that column into the body of a report or analysis? The name will wrap unattractively, making the header row very fat. Or it will shrink down to a font so tiny that no one can read it. And then the user will rename the column, violating our key rule that each object has one name.

I try to limit column names to 30 characters, though sometimes I go to 35. In order to achieve this goal, I have to register more abbreviations or acronyms than I would like.

8. Consider prepending column names with an abbreviated table name.
I hate to make this recommendation, because it violates several of my previous rules about abbreviations and short names. But I am finding myself following this practice with increasing frequency in order to guarantee consistency and uniqueness.

9. Change names in the view layer if needed.
We have always recommended a set of views in the DW/BI system which sit atop the physical tables and to which all queries are directed. The primary purpose of the view layer is to provide a layer of insulation between the BI applications and the physical database, providing a bit of flexibility to smoothly migrate change to a system already in production. Additionally, the view layer can also provide a place to put the business-oriented names into the database.

Our first recommendation is always to name the physical tables and columns with business-oriented names. Failing that, use the view layer. We dislike changing the names in the BI tools for several reasons:

    Most organizations have several BI tools; the names should be consistent across all BI tools.
    The more business logic you put into the BI tool, the more challenging it will be to migrate to a different tool.
    If the names are only in the BI tool, there is a barrier to communication between users, front room support team, and back room database people.

10. Be consistent!
It’s only a foolish consistency that’s the hobgoblin of little minds. Consistency in naming is hugely valuable to your users.
