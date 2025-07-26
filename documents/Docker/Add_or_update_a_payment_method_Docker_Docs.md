# Add or update a payment method | Docker Docs

**URL:** http://docs.docker.com/billing/payment-method
**Word Count:** 2070
**Links Count:** 668
**Scraped:** 2025-07-16 02:08:04
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](http://docs.docker.com/get-started/)   * [Guides](http://docs.docker.com/guides/)   * [Reference](http://docs.docker.com/reference/)

* * *

# Add or update a payment method

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

This page describes how to add or update a payment method for your personal account or for an organization.

You can add a payment method or update your account's existing payment method at any time.

> Important >  > If you want to remove all payment methods, you must first downgrade your subscription to a free subscription. See [Downgrade](https://docs.docker.com/subscription/change/).

The following payment methods are supported:

  * Cards     * Visa     * MasterCard     * American Express     * Discover     * JCB     * Diners     * UnionPay   * Wallets     * Stripe Link   * Bank accounts     * ACH transfer with a [verified](https://docs.docker.com/billing/payment-method/#verify-a-bank-account) US bank account

All currency, for example the amount listed on your billing invoice, is in United States dollar \(USD\).

> Important >  > For United States customers, Docker began collecting sales tax on July 1, 2024. For European customers, Docker began collecting VAT on March 1, 2025. For United Kingdom customers, Docker began collecting VAT on May 1, 2025. >  > To ensure that tax assessments are correct, make sure that your [billing information](http://docs.docker.com/billing/details/) and VAT/Tax ID, if applicable, are updated. If you're exempt from sales tax, see [Register a tax certificate](http://docs.docker.com/billing/tax-certificate/).

## Manage payment method

### Personal account

Docker subscription  Legacy Docker subscription

To add a payment method:

  1. Sign in to [Docker Home](https://app.docker.com/) and select your organization.   2. Select **Billing**.   3. Select **Payment methods** from the left-hand menu.   4. Select **Add payment method**.   5. Enter your new payment information:      * If you are adding a card:        * Select **Card** and fill out the card information form.      * If you are adding a Link payment:        * Select **Secure, 1-click checkout with Link** and enter your Link **email address** and **phone number**.        * If you are not an existing Link customer, you must fill out the card information form to store a card for Link payments.      * If you are adding a bank account:        * Select **US bank account**.        * Verify your **Email** and **Full name**.        * If your bank is listed, select your bank's name.        * If your bank is not listed, select **Search for your bank**.        * To verify your bank account, see [Verify a bank account](https://docs.docker.com/billing/payment-method/#verify-a-bank-account).   6. Select **Add payment method**.   7. Optional. You can set a new default payment method by selecting the **Set as default** action.   8. Optional. You can remove non-default payment methods by selecting the **Delete** action.

> Note >  > If you want to set a US bank account as your default payment method, you must verify the account first.

To add a payment method:

  1. Sign in to [Docker Hub](https://hub.docker.com).   2. Select **Billing**.   3. Select the **Payment methods** link.   4. Select **Add payment method**.   5. Enter your new payment information:      * If you are adding a card:        * Select **Card** and fill out the card information form.      * If you are adding a Link payment:        * Select **Secure, 1-click checkout with Link** and enter your Link **email address** and **phone number**.        * If you are not an existing Link customer, you must fill out the card information form to store a card for Link payments.   6. Select **Add**.   7. Select the **Actions** icon, then select **Make default** to ensure that your new payment method applies to all purchases and subscriptions.   8. Optional. You can remove non-default payment methods by selecting the **Actions** icon. Then, select **Delete**.

### Organization

> Note >  > You must be an organization owner to make changes to the payment information.

Docker subscription  Legacy Docker subscription

To add a payment method:

  1. Sign in to [Docker Home](https://app.docker.com/) and select your organization.   2. Select **Billing**.   3. Select **Payment methods** from the left-hand menu.   4. Select **Add payment method**.   5. Enter your new payment information:      * If you are adding a card:        * Select **Card** and fill out the card information form.      * If you are adding a Link payment:        * Select **Secure, 1-click checkout with Link** and enter your Link **email address** and **phone number**.        * If you are not an existing Link customer, you must fill out the card information form to store a card for Link payments.      * If you are adding a bank account:        * Select **US bank account**.        * Verify your **Email** and **Full name**.        * If your bank is listed, select your bank's name.        * If your bank is not listed, select **Search for your bank**.        * To verify your bank account, see [Verify a bank account](https://docs.docker.com/billing/payment-method/#verify-a-bank-account).   6. Select **Add payment method**.   7. Select **Add payment method**.   8. Optional. You can set a new default payment method by selecting the **Set as default** action.   9. Optional. You can remove non-default payment methods by selecting the **Delete** action.

> Note >  > If you want to set a US bank account as your default payment method, you must verify the account first.

To add a payment method:

  1. Sign in to [Docker Hub](https://hub.docker.com).   2. Select your organization, then select **Billing**.   3. Select the **Payment methods** link.   4. Select **Add payment method**.   5. Enter your new payment information:      * If you are adding a card:        * Select **Card** and fill out the card information form.      * If you are adding a Link payment:        * Select **Secure, 1-click checkout with Link** and enter your Link **email address** and **phone number**.        * If you are not an existing Link customer, you must fill out the card information form to store a card for Link payments.   6. Select **Add payment method**.   7. Select the **Actions** icon, then select **Make default** to ensure that your new payment method applies to all purchases and subscriptions.   8. Optional. You can remove non-default payment methods by selecting the **Actions** icon. Then, select **Delete**.

## Verify a bank account

There are two ways to verify a bank account as a payment method:

  * Instant verification: Docker supports several major banks for instant verification.   * Manual verification: All other banks must be verified manually.

### Instant verification

To verify your bank account instantly, you must sign in to your bank account from the Docker billing flow:

  1. Choose **US bank account** as your payment method.   2. Verify your **Email** and **Full name**.   3. If your bank is listed, select your bank's name or select **Search for your bank**.   4. Sign in to your bank and review the terms and conditions. This agreement allows Docker to debit payments from your connected bank account.   5. Select **Agree and continue**.   6. Select an account to link and verify, and select **Connect account**.

When the account is verified, you will see a success message in the pop-up modal.

### Manual verification

To verify your bank account manually, you must enter the micro-deposit amount from your bank statement:

  1. Choose **US bank account** as your payment method.   2. Verify your **Email** and **First and last name**.   3. Select **Enter bank details manually instead**.   4. Enter your bank details: **Routing number** and **Account number**.   5. Select **Submit**.   6. You will receive an email with instructions on how to manually verify.

Manual verification uses micro-deposits. You should see a small deposit \(e.g. $-0.01\) in your bank account in 1-2 business days. Open your manual verification email and enter the amount of this deposit to verify your account.

## Failed payments

> Note >  > You can't manually retry a failed payment. Docker will retry failed payments based on the retry schedule.

If your subscription payment fails, there is a grace period of 15 days, including the due date. Docker retries to collect the payment 3 times using the following schedule:

  * 3 days after the due date   * 5 days after the previous attempt   * 7 days after the previous attempt

Docker also sends an email notification `Action Required - Credit Card Payment Failed` with an attached unpaid invoice after each failed payment attempt.

Once the grace period is over and the invoice is still not paid, the subscription downgrades to a free subscription and all paid features are disabled.

## Redeem a coupon

You can redeem a coupon for any paid Docker subscription.

A coupon can be used when you:

  * Sign up to a new paid subscription from a free subscription   * Upgrade an existing paid subscription

You are asked to enter your coupon code when you confirm or enter your payment method.

If you use a coupon to pay for a subscription, when the coupon expires, your payment method is charged the full cost of your subscription. If you don't have a saved payment method, your account downgrades to a free subscription.